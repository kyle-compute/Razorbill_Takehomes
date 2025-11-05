# PDF to JSON Converter - Interview Take Home

## Overview

*This assignment is intentionally vague to test your ability to work with existing data structures. You have the existing converted data as reference - understand the pattern and build a converter that can process bulk PDFs.*

Build a robust PDF-to-JSON converter that can process scraped medical policy PDFs and extract structured data for analysis. This tests your ability to parse complex documents, maintain data consistency, and handle processing at scale.

**Goal**: Convert scraped PDFs into structured JSON format for downstream RAG/analysis systems.

## What We're Looking For

- Understanding of existing data patterns from converted examples
- Robust PDF parsing and text extraction
- Intelligent chunking and metadata extraction
- Error handling for malformed or difficult PDFs
- Clean data structure matching existing patterns

## Core Deliverables

### 1. PDF Processing Pipeline
Build a converter that can:
- Extract clean text from medical policy PDFs
- Identify document structure (sections, headings, lists)
- Extract medical codes, dates, and key metadata
- Handle different PDF layouts and formats

### 2. Output Generation
For each PDF processed, generate:
- **Metadata file**: Policy-level information following existing pattern
- **Content chunks**: Text broken into logical sections with metadata
- Proper JSON structure matching existing converted data

### 3. Processing Features
- Bulk processing capabilities for entire directories
- Progress tracking and logging
- Error handling for problematic PDFs
- Data validation and sanitization

## Reference Data Structure

**Existing Data Location**: `/home/tax/Desktop/razorbill/convert/RAG/`

### Example Metadata Pattern
```json
{
  "policy_id": "SUR703.005",
  "version_date": "2024-10-15",
  "title": "Heart Transplant",
  "category": "surgery",
  "local_pdf_path": "../../output/pdfs/SUR703.005_2024-10-15.pdf",
  "codes": {
    "cpt": [],
    "hcpcs": ["S2152"]
  },
  "keywords": {
    "conditions": ["trauma", "transplant", "stroke"],
    "procedures": [],
    "coverage_terms": ["medically necessary", "may be considered"]
  },
  "page_url": "https://medicalpolicy.hcsc.com/...",
  "pdf_url": "https://medicalpolicy.hcsc.com/..."
}
```

### Example Content Chunks Pattern
```json
[
  {
    "chunk_id": "SUR703.005_2024-10-15_chunk_001",
    "policy_id": "SUR703.005",
    "version_date": "2024-10-15",
    "text": "Human heart transplant may be considered medically necessary...",
    "section": "Coverage",
    "page": 1,
    "title": "Heart Transplant",
    "category": "surgery",
    "codes": { "cpt": [], "hcpcs": ["S2152"] },
    "keywords": { /* extracted keywords */ },
    "summary": "Human heart transplant may be considered..."
  }
]
```

## Technical Constraints

**Study the Reference Data:**
- Examine existing converted files in `/home/tax/Desktop/razorbill/convert/RAG/`
- Understand the metadata schema and chunking patterns
- Follow the same naming conventions and file structure

**Required Functionality:**
- Use `pdfplumber` or similar for reliable text extraction
- Implement intelligent section detection and chunking
- Extract medical codes (CPT, HCPCS) and keywords
- Handle PDFs with varying layouts and quality
- Maintain data sanitization practices (see REQUIREMENTS.md)

**Processing Requirements:**
- Process PDFs from `/home/tax/Desktop/razorbill/output/pdfs/`
- Generate output in same structure as existing converted data
- Include progress logging and error reporting
- Handle edge cases gracefully

## Submission Requirements

### Code Implementation
- Well-structured Python converter script
- Configuration for different input/output paths
- Modular functions for extraction, chunking, and validation
- Basic unit tests for core functionality

### Sample Output
- Demonstrate conversion of 5-10 sample PDFs
- Show both metadata and chunk outputs
- Include before/after examples of your conversion

### Documentation
Briefly explain:
- Your approach to PDF text extraction
- How you identify document sections and structure
- Method for extracting codes and keywords
- Any challenges encountered and solutions

## Evaluation Criteria

1. **Data Quality (40%)** - Accuracy and completeness of extracted information
2. **Code Quality (30%)** - Clean, maintainable, well-documented implementation
3. **Pattern Consistency (20%)** - How well you match existing data structures
4. **Error Handling (10%)** - Robustness with problematic PDFs

## Input Data Access

**Source PDFs**: `/home/tax/Desktop/razorbill/output/pdfs/`
**Reference Output**: `/home/tax/Desktop/razorbill/convert/RAG/metadata/` and `/home/tax/Desktop/razorbill/convert/RAG/chunks/`

You have access to examine the existing converted data to understand the expected patterns and structures.

## Notes

- **Focus on quality over quantity** - better to have 10 perfectly converted policies than 50 poorly ones
- **Pattern matching is key** - study the existing data structures carefully
- **Medical content complexity** - these are technical medical documents, handle with appropriate care
- **You will not be penalized** for PDFs that are truly unreadable or malformed - log these appropriately

This should take approximately 3-5 hours. Focus on demonstrating your ability to understand existing patterns and build reliable data conversion tools.

## Example Processing Flow

1. **Read PDF**: Extract raw text and structure
2. **Identify Metadata**: Extract policy ID, dates, title, codes
3. **Section Detection**: Identify Coverage, Guidelines, Coding sections
4. **Chunk Creation**: Break content into logical pieces
5. **Keyword Extraction**: Identify medical terms and conditions
6. **Validation**: Ensure output matches existing patterns
7. **Save Results**: Generate metadata and chunk JSON files