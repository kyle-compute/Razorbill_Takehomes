# Razorbill Take Home Assignments

*We believe projects demonstrate skills better than credentials. Choose one option below that best showcases your abilities.*

## Development Standards

- **PEP-8 compliance** - Clean, readable Python code
- **Modular architecture** - Files <140 lines, clear separation of concerns
- **Docker + UV** - Use our established Docker patterns with UV package manager
- **Security-first** - Follow sanitization patterns in [REQUIREMENTS.md](REQUIREMENTS.md:55)

## Option 1: PDF to JSON Converter

### The Challenge
Convert scraped medical policy PDFs into structured JSON for RAG/analysis systems.

### What You'll Build
- **PDF Processor**: Extract clean text from complex medical documents
- **Metadata Extractor**: Identify policy IDs, dates, medical codes, keywords
- **Content Chunker**: Break policies into logical sections
- **Bulk Converter**: Process entire directories efficiently

### Reference Examples
```bash
# Study the existing conversion patterns
ls convert/examples/
# ├── SUR703.005_2024-10-15.json      # Metadata output
# ├── SUR703.005_2024-10-15_chunks.json # Content chunks
# ├── SUR703.005_2024-10-15.pdf         # Source PDF
# └── README.md                         # Analysis guide
```

### Key Skills Tested
- PDF parsing with `pdfplumber`
- Medical content extraction (CPT/HCPCS codes, conditions, procedures)
- Data structure consistency
- Error handling for malformed documents

### Expected Output
Match existing patterns exactly:
```json
{
  "policy_id": "SUR703.005",
  "version_date": "2024-10-15",
  "title": "Heart Transplant",
  "category": "surgery",
  "codes": {"cpt": [], "hcpcs": ["S2152"]},
  "keywords": {"conditions": ["trauma", "transplant"]}
}
```

---

## Option 2: Health Insurance Web Scraper

### The Challenge
Build a daily-running scraper for major health insurance providers' medical policies.

### Target Providers
- **UnitedHealthcare (UHC)**: https://www.uhc.com/
- **Blue Cross Blue Shield**: https://www.bcbs.com/
- **Aetna**: https://www.aetna.com/
- **Medicaid**: https://www.medicaid.gov/

### Daily Automation Requirements
- **Cron/Scheduled**: Run once every 24 hours
- **Rate Limiting**: Respect robots.txt, implement delays
- **Incremental Updates**: Only download new/changed policies
- **Error Recovery**: Retry failed downloads, log issues

### Reference Implementation
Study the HCSC scraper pattern:
```bash
# Base scraper structure to adapt
ls hcsc_scraper/
# ├── scraper.py     # Main scraper class
# ├── test_scraper.py # Testing script
# └── output/         # Sample data structure
```

### Key Skills Tested
- Multi-site scraping with different authentication patterns
- Robust error handling and retry logic
- Rate limiting and ethical scraping practices
- Data deduplication and change detection

### Daily Workflow
```python
# Example daily automation
def daily_scrape():
    for provider in [UHC, BCBS, Aetna, Medicaid]:
        scraper = ProviderScraper(provider)
        new_policies = scraper.check_for_updates()
        if new_policies:
            scraper.download_policies(new_policies)
            scraper.notify_updates()
```

---

## Option 3: End-to-End Pipeline (Ambitious)

### The Full Challenge
**Not required, but impressive if completed:** Build a complete automated pipeline:

1. **Daily Web Scraping** (Option 2)
2. **PDF to JSON Conversion** (Option 1)
3. **Vector Database Storage** with embeddings
4. **Automated Notifications** for policy changes

### Advanced Skills
- **Container Orchestration**: Docker Compose with multiple services
- **Vector Search**: pgvector + embeddings for semantic search
- **Scheduled Workflows**: Cron + monitoring/alerting
- **Data Pipeline**: ETL with error handling and monitoring

### Architecture Example
```yaml
# docker-compose.yml structure
services:
  scraper:
    build: ./scraper
    cron: "0 2 * * *"  # Daily at 2 AM

  converter:
    build: ./converter
    depends_on: [scraper]

  database:
    image: pgvector/pgvector:pg16

  embeddings:
    build: ./embeddings
    depends_on: [database, converter]
```

---

## Docker + UV Setup

### Required Pattern (Following Main Repo)
```dockerfile
# Use the established Razorbill pattern
FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Install UV package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Your application code
WORKDIR /app
COPY requirements.txt .
RUN uv pip install -r requirements.txt
```

### Dependencies Management
```bash
# Use UV for dependency management
uv add requests beautifulsoup4 pdfplumber
uv add --dev pytest black flake8
```

### Running Your Solution
```bash
# Development
uv run python main.py

# Docker (required for final submission)
docker build -t my-solution .
docker run -v $(pwd)/output:/app/output my-solution
```

---

## Submission Guidelines

### What to Submit
1. **Git Repository** with clear README
2. **Dockerfile** following Razorbill patterns
3. **Sample Output** demonstrating functionality
4. **Brief Documentation** of your approach

### File Structure
```
your-solution/
├── README.md              # Your approach + setup
├── Dockerfile             # Following Razorbill pattern
├── pyproject.toml         # UV dependencies
├── src/                   # Your modular code
├── tests/                 # Quality tests
├── examples/              # Sample output
└── docker-compose.yml     # If multi-service (Option 3)
```

### Evaluation Criteria
1. **Working Solution (40%)** - Does it solve the problem?
2. **Code Quality (30%)** - Clean, maintainable architecture
3. **Technical Skills (20%)** - Docker, UV, security practices
4. **Documentation (10%)** - Clear explanation of approach

### Focus Areas by Option
- **Option 1**: Data extraction accuracy, pattern matching
- **Option 2**: Scraping robustness, rate limiting ethics
- **Option 3**: System architecture, end-to-end automation

Choose the option that best showcases your strengths. We value thoughtful, working solutions over complex, broken ones.

