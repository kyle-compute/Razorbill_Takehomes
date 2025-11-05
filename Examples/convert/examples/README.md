# Example Data for PDF-to-JSON Converter

## Reference Files

These are actual examples from the existing conversion system to help you understand the expected output format.

### Metadata Examples
- **SUR703.005_2024-10-15.json** - Surgery policy (Heart Transplant)
- **ADM1001.005_2024-06-15.json** - Administrative policy (Ambulance Services)
- **DME101.000_2024-11-15.json** - DME policy (Durable Medical Equipment)

### Content Chunks Examples
- **SUR703.005_2024-10-15_chunks.json** - Chunked content for Heart Transplant policy
- **ADM1001.005_2024-06-15_chunks.json** - Chunked content for Ambulance Services policy
- **DME101.000_2024-11-15_chunks.json** - Chunked content for DME policy

### Source PDFs
- **SUR703.005_2024-10-15.pdf** - Source PDF for Heart Transplant policy
- **ADM1001.005_2024-06-15.pdf** - Source PDF for Ambulance Services policy
- **DME101.000_2024-11-15.pdf** - Source PDF for DME policy

## Study These Examples

1. **Examine the PDF structure** - Look at how the source PDFs are organized
2. **Compare to JSON output** - See how the PDF content was extracted and structured
3. **Understand the metadata schema** - Policy info, codes, keywords, URLs
4. **Analyze chunking strategy** - How text is broken into logical sections
5. **Note data patterns** - What information is consistently extracted

Your converter should produce output that matches these patterns exactly.