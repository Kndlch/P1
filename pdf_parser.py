from PyPDF2 import PdfReader
import re
#import tkinter as tk
#from tkinter import filedialog


def parse_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def search_keywords(text, keywords):
    results = []
    for keyword in keywords:
        pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)
        matches = re.finditer(pattern, text)
        for match in matches:
            results.append((match.group(), match.start(), match.end()))
    return results

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)


if __name__ == '__main__':
    file_path = input('Enter the path to the PDF file: ')
    keywords = input("Enter the keywords to search (comma-separated): ").split(',')
    text = parse_pdf(file_path)
    results = search_keywords(text, keywords)
    print("Search results:")
    for result in results:
        print(f"Page: {result[0]}, Start: {result[1]}, End: {result[2]}")

