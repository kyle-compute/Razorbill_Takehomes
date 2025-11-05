"""HCSC Medical Policy Scraper

Scrapes medical policies from https://medicalpolicy.hcsc.com/
Downloads PDFs and extracts metadata for each policy.
"""

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse, parse_qs

import requests
from bs4 import BeautifulSoup


class HCSCScraper:
    """Scraper for HCSC Medical Policies"""

    BASE_URL = "https://medicalpolicy.hcsc.com"
    INDEX_URL = "https://medicalpolicy.hcsc.com/active-policies?corpEntCd=HCSC"

    def __init__(self, output_dir: str = "output"):
        """Initialize the scraper

        Args:
            output_dir: Directory to save PDFs and metadata
        """
        self.output_dir = Path(output_dir)
        self.pdfs_dir = self.output_dir / "pdfs"
        self.metadata_dir = self.output_dir / "metadata"

        # Create output directories
        self.pdfs_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_dir.mkdir(parents=True, exist_ok=True)

        # Setup session with cookie to bypass disclaimer
        self.session = requests.Session()
        self.session.cookies.set(
            "medicalpolicy_disclaimer_accept_HCSC",
            "YES",
            domain="medicalpolicy.hcsc.com",
            path="/"
        )
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def get_policy_links(self) -> List[Dict[str, str]]:
        """Fetch the index page and extract all policy links

        Returns:
            List of dicts with 'url' and 'title' keys
        """
        print(f"Fetching index page: {self.INDEX_URL}")
        response = self.session.get(self.INDEX_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')

        # Find all policy links
        # The actual structure will depend on the page content after accepting disclaimer
        policy_links = []

        # Look for links that point to policy pages
        # Common patterns: activePolicyPage, policy details, etc.
        for link in soup.find_all('a', href=True):
            href = link['href']

            # Filter for policy page links
            if 'activePolicyPage' in href or 'policy' in href.lower():
                full_url = urljoin(self.BASE_URL, href)
                title = link.get_text(strip=True)

                if full_url not in [p['url'] for p in policy_links]:
                    policy_links.append({
                        'url': full_url,
                        'title': title or 'Untitled'
                    })

        print(f"Found {len(policy_links)} policy links")
        return policy_links

    def extract_policy_metadata(self, url: str) -> Optional[Dict]:
        """Extract metadata and PDF URL from a policy page

        Args:
            url: URL of the policy page

        Returns:
            Dict with metadata including pdf_url, or None if no PDF found
        """
        print(f"Extracting metadata from: {url}")

        try:
            response = self.session.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')

            metadata = {
                'page_url': url,
                'pdf_url': None,
                'title': None,
                'policy_id': None,
                'effective_date': None,
                'category': None,
            }

            # Extract policy details from the path parameter
            # Pattern: activePolicyPage?path=medicine/MED207.118_2025-04-01&corpEntCd=HCSC
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            if 'path' in query_params:
                path = query_params['path'][0]

                # Construct PDF URL
                # Becomes: /content/dam/bcbs/medicalpolicy/pdf/medicine/MED207.118_2025-04-01.pdf
                pdf_path = f"/content/dam/bcbs/medicalpolicy/pdf/{path}.pdf"
                metadata['pdf_url'] = urljoin(self.BASE_URL, pdf_path)

                # Extract policy ID and category from path (e.g., surgery/SUR706.017_2024-12-15)
                parts = path.split('/')
                if len(parts) > 1:
                    policy_file = parts[-1]
                    metadata['category'] = parts[0]  # First part is category
                    metadata['policy_id'] = policy_file

            # Extract title from page
            title_elem = soup.find('h1') or soup.find('title')
            if title_elem:
                metadata['title'] = title_elem.get_text(strip=True)

            # Look for effective date in the page
            date_text = soup.find(string=lambda s: s and 'effective' in s.lower())
            if date_text:
                metadata['effective_date'] = date_text.strip()

            return metadata

        except Exception as e:
            print(f"Error extracting metadata from {url}: {e}")
            return None

    def download_pdf(self, pdf_url: str, metadata: Dict) -> Optional[str]:
        """Download a PDF file

        Args:
            pdf_url: URL of the PDF
            metadata: Metadata dict for naming the file

        Returns:
            Path to downloaded file, or None if failed
        """
        try:
            print(f"Downloading PDF: {pdf_url}")

            response = self.session.get(pdf_url, stream=True)
            response.raise_for_status()

            # Generate filename from policy ID or URL
            if metadata.get('policy_id'):
                filename = f"{metadata['policy_id']}.pdf"
            else:
                # Extract from URL
                filename = os.path.basename(urlparse(pdf_url).path)

            filepath = self.pdfs_dir / filename

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Saved to: {filepath}")
            return str(filepath)

        except Exception as e:
            print(f"Error downloading PDF from {pdf_url}: {e}")
            return None

    def save_metadata(self, metadata: Dict, pdf_path: Optional[str] = None):
        """Save metadata to JSON file

        Args:
            metadata: Metadata dict
            pdf_path: Path to downloaded PDF file
        """
        if pdf_path:
            metadata['local_pdf_path'] = pdf_path

        # Generate filename
        if metadata.get('policy_id'):
            filename = f"{metadata['policy_id']}.json"
        else:
            # Use hash of URL
            import hashlib
            url_hash = hashlib.md5(metadata['page_url'].encode()).hexdigest()[:8]
            filename = f"policy_{url_hash}.json"

        filepath = self.metadata_dir / filename

        with open(filepath, 'w') as f:
            json.dump(metadata, f, indent=2)

        print(f"Saved metadata to: {filepath}")

    def scrape_all(self, delay: float = 1.0):
        """Main scraping function - scrapes all policies

        Args:
            delay: Delay in seconds between requests
        """
        print("Starting HCSC Medical Policy scraper...")

        # Get all policy links
        policy_links = self.get_policy_links()

        if not policy_links:
            print("No policy links found. The page structure may have changed.")
            return

        # Process each policy
        for i, policy_link in enumerate(policy_links, 1):
            print(f"\n[{i}/{len(policy_links)}] Processing: {policy_link['title']}")

            # Extract metadata
            metadata = self.extract_policy_metadata(policy_link['url'])

            if not metadata:
                print("Failed to extract metadata, skipping...")
                continue

            # Download PDF if available
            pdf_path = None
            if metadata.get('pdf_url'):
                pdf_path = self.download_pdf(metadata['pdf_url'], metadata)
            else:
                print("No PDF URL found on this page")

            # Save metadata
            self.save_metadata(metadata, pdf_path)

            # Be polite - add delay between requests
            if i < len(policy_links):
                time.sleep(delay)

        print(f"\nScraping complete! Downloaded {len(policy_links)} policies.")
        print(f"PDFs saved to: {self.pdfs_dir}")
        print(f"Metadata saved to: {self.metadata_dir}")


def main():
    """Main entry point"""
    scraper = HCSCScraper(output_dir="output")
    scraper.scrape_all(delay=1.0)


if __name__ == "__main__":
    main()
