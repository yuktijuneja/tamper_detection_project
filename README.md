# Tamper Detection in Academic Credentials

What it does:
Detects tampering in academic PDFs using:

- Metadata comparison
- OCR text anomaly detection

Setup:

```bash
pip install -r requirements.txt



This project demonstrates tamper detection techniques for academic documents using Python. The system detects tampering by analyzing:

- PDF metadata (e.g., creation and modification dates)
- Visual content and layout irregularities using OCR-based text comparison

---

## Project Structure

tamper-detection-academic-credentials/
├── src/ # Python scripts
│ ├── metadata_check.py # PDF metadata tamper detection
│ └── ocr_anomaly_detect.py # OCR-based text anomaly detection
├── samples/ # Sample original and tampered PDFs
│ ├── degree_original.pdf
│ ├── degree_tampered.pdf
│ ├── transcript_original.pdf
│ └── transcript_tampered.pdf
├── reports/ # Project reports
│ └── technical_report.pdf
├── demo/ # demo video files
├── README.md # This file
└── requirements.txt # Python dependencies


---

## Features

- PDF Metadata Checker: Detects inconsistencies in PDF metadata such as creation and modification dates which may indicate tampering.
- OCR Text Comparator: Extracts text from PDFs and compares original vs tampered versions to identify text changes.

---
```
