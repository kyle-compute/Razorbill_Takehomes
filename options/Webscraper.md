# Health Insurance Web Scraper - Interview Take Home

## Overview

*This assignment is intentionally vague to test your problem-solving abilities. You have the HCSC scraper as a reference point - adapt those patterns to work with other major health insurance providers.*

Build a web scraper that can collect medical policy information from major health insurance providers. This tests your ability to work with different website structures while maintaining code quality and ethical scraping practices.

**Target Providers:**
- UnitedHealthcare (UHC)
- Blue Cross Blue Shield (BCBS)
- Aetna
- Medicaid

## What We're Looking For

- Ability to reverse-engineer website structures independently
- Clean, maintainable code architecture
- Proper error handling and rate limiting
- Thoughtful data organization and metadata extraction
- Following security/sanitization best practices (see REQUIREMENTS.md)

## Core Deliverables

### 1. Working Scrapers
Create scrapers for the providers above that can:
- Navigate to medical policy sections on each site
- Extract policy documents and metadata
- Handle different document formats (PDF, HTML, etc.)
- Implement proper rate limiting and error handling

### 2. Metadata Collection
For each policy found, extract and save:
- Policy title and identifier
- Effective date(s)
- Category/classification
- Source URL
- Document type
- Download timestamp
- Any other relevant metadata you discover

### 3. Output Structure
Organize your output with:
- Downloaded documents (PDFs, HTML saves)
- Metadata files (JSON format preferred)
- Clear file naming and directory structure
- Deduplication logic

## Technical Constraints

**Keep It Simple & Effective:**
- Don't over-engineer - focus on working solutions
- Use the HCSC scraper as a pattern reference, not a template to copy
- Handle challenges as you encounter them (authentication, dynamic content, etc.)
- Document your approach and any blockers

**Required Practices:**
- Implement proper rate limiting (be respectful to servers)
- Handle errors gracefully with retry logic
- Sanitize all inputs and outputs
- Include basic logging
- Follow the security patterns outlined in REQUIREMENTS.md

## Submission Requirements

### Code Repository
- Well-structured Python code
- Clear README with setup instructions
- Requirements.txt with dependencies
- Basic tests (quality over quantity)

### Sample Output
- Demonstrate successful scraping from at least 2 providers
- Include sample metadata and downloaded documents
- Show your output organization approach

### Documentation
Briefly explain:
- Your overall approach
- Challenges encountered and how you solved them
- Any assumptions or limitations
- How to run your scrapers

## Evaluation Criteria

1. **Working Solution (40%)** - Does it actually scrape and collect data?
2. **Code Quality (30%)** - Clean, maintainable, well-documented code
3. **Problem Solving (20%)** - How did you handle the inevitable challenges?
4. **Security & Ethics (10%)** - Proper sanitization, rate limiting, responsible scraping

## Notes

- **You will not be penalized** for scraping challenges beyond your control (CAPTCHAs, site changes, etc.) - document these issues
- **Quality over quantity** - better to have 2 working scrapers than 4 broken ones
- **Be creative** in how you handle different site structures and authentication patterns
- **Ask questions** if you need clarification on expectations vs. requirements

This should take approximately 4-6 hours. Focus on demonstrating your approach to problem-solving and building maintainable scraping solutions.