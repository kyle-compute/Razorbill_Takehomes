"""Test script to verify scraper works on a few policies"""

from scraper import HCSCScraper

def test_scraper():
    """Test the scraper on first 3 policies"""
    scraper = HCSCScraper(output_dir="test_output")

    # Get policy links
    policy_links = scraper.get_policy_links()

    if not policy_links:
        print("No policy links found!")
        return

    # Test with first 3 policies
    print(f"\nTesting with first 3 of {len(policy_links)} policies...\n")

    for i, policy_link in enumerate(policy_links[:3], 1):
        print(f"[{i}/3] Testing: {policy_link['title']}")
        print(f"URL: {policy_link['url']}")

        # Extract metadata
        metadata = scraper.extract_policy_metadata(policy_link['url'])

        if not metadata:
            print("Failed to extract metadata\n")
            continue

        print(f"Title: {metadata.get('title')}")
        print(f"Policy ID: {metadata.get('policy_id')}")
        print(f"Category: {metadata.get('category')}")
        print(f"PDF URL: {metadata.get('pdf_url')}")

        # Download PDF if available
        pdf_path = None
        if metadata.get('pdf_url'):
            pdf_path = scraper.download_pdf(metadata['pdf_url'], metadata)
            if pdf_path:
                print(f"Downloaded PDF: {pdf_path}")
        else:
            print("No PDF URL found")

        # Save metadata
        scraper.save_metadata(metadata, pdf_path)
        print()

if __name__ == "__main__":
    test_scraper()
