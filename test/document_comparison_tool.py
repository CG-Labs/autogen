import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader
import docx

# Ensure necessary NLTK data files are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def extract_key_points(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    return filtered_words

def compare_documents(doc1, doc2):
    key_points1 = extract_key_points(doc1)
    key_points2 = extract_key_points(doc2)

    common_points = set(key_points1).intersection(set(key_points2))
    unique_to_doc1 = set(key_points1) - set(key_points2)
    unique_to_doc2 = set(key_points2) - set(key_points1)

    return {
        "common_points": common_points,
        "unique_to_doc1": unique_to_doc1,
        "unique_to_doc2": unique_to_doc2
    }

def generate_report(comparison_result):
    report = "Comparison Report:\n\n"
    report += "Common Points:\n"
    report += "\n".join(comparison_result["common_points"]) + "\n\n"
    report += "Unique to Document 1:\n"
    report += "\n".join(comparison_result["unique_to_doc1"]) + "\n\n"
    report += "Unique to Document 2:\n"
    report += "\n".join(comparison_result["unique_to_doc2"]) + "\n"
    return report

# Example usage
if __name__ == "__main__":
    doc1_text = read_txt("sample1.txt")
    doc2_text = read_txt("sample2.txt")

    comparison_result = compare_documents(doc1_text, doc2_text)
    report = generate_report(comparison_result)

    print(report)
