import io
from PyPDF2 import PdfReader

def parse_resume_text(file_storage):
    """
    Extracts text from PDF file sent as Werkzeug FileStorage (Flask file upload)
    :param file_storage: Flask request.files['resume'] object
    :return: extracted plain text string from PDF
    """

    # Read file bytes from FileStorage stream
    file_bytes = file_storage.read()

    # Use PdfReader to extract text
    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Reset file pointer for any future use
    file_storage.stream.seek(0)

    return text.strip()


if __name__ == "__main__":
    # Simple test with a local PDF file
    with open("sample_resume.pdf", "rb") as f:
        class DummyFileStorage:
            def read(self_inner):
                return f.read()
            def stream(self_inner):
                f.seek(0)
        dummy_file = DummyFileStorage()
        extracted_text = parse_resume_text(dummy_file)
        print(extracted_text)
