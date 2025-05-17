from PyPDF2 import PdfReader
import os

def analyze_metadata(path):
    reader = PdfReader(path)
    metadata = reader.metadata
    print(f"Metadata for {path}:\n")
    for key, value in metadata.items():
        print(f"{key}: {value}")
    if "/ModDate" in metadata and "/CreationDate" in metadata:
        if metadata["/ModDate"] != metadata["/CreationDate"]:
            print("Possible tampering: ModDate differs from CreationDate")
        else:
            print("No tampering detected in metadata.")

if __name__ == "__main__":
    folder = "samples"
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            analyze_metadata(os.path.join(folder, filename))
            print("-" * 50)
