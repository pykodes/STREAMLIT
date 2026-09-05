# PDF and Word Converter
A Streamlit application for converting PDF files to Word documents and Word documents to PDF files.

## Features
- PDF to DOCX conversion with `pdf2docx`
- DOCX to PDF conversion with `python-docx` and ReportLab
- Browser-based uploads and downloads through Streamlit
- 
- # Requirements
- Python 3.14.5 (the version used when this README was prepared)

The application dependencies are pinned to the versions installed in the development environment:

| Package | Version | Used for |
| --- | --- | --- |
| `streamlit` | `1.63.0` | Web interface, upload controls, tabs, messages, and downloads |
| `pdf2docx` | `0.5.13` | PDF to DOCX conversion |
| `python-docx` | `1.2.0` | Reading DOCX paragraph content |
| `reportlab` | `5.0.1` | Creating PDF files |

`tempfile` is also imported by `app.py`. It is part of Python's standard library and does not need to be installed separately.
