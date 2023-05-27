import PyPDF2
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog
import re



window = tk.Tk()
window.title("PDF Parser")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

select_button = tk.Button(window, text="Select File", command=select_file)
select_button.grid(row=0, column=0, pady=10, padx=10)

file_path_label = tk.Label(window, text="File Path:")
file_path_label.grid(row=1, column=0)

file_path_entry = tk.Entry(window, width=50)
file_path_entry.grid(row=1, column=1, padx=10)

def parse_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def search_keywords():

    file_path = file_path_entry.get()
    keywords = keyword_entry.get().split(',')
    text = parse_pdf(file_path)
    
    results = []
    for keyword in keywords:
        pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)
        matches = re.finditer(pattern, text)
        for match in matches:
            results.append((match.group(), match.start(), match.end()))
    
    
    results_text.delete(1.0, tk.END)  # Clear previous results

    if results:
        for result in results:
            page_num, start, end = result
            result_text = f"Page: {page_num}, Start: {start}, End: {end}\n"
            results_text.insert(tk.END, result_text)
    else:
        results_text.insert(tk.END, "No results found.")

#* Create label and entry for keyword input
keyword_label = tk.Label(window, text="Keywords:")
keyword_label.grid(row=2, column=0)

keyword_entry = tk.Entry(window, width=50)
keyword_entry.grid(row=2, column=1, padx=10)

#* Create Search button
search_button = tk.Button(window, text="Search", command=search_keywords)
search_button.grid(row=3, column=0, pady=10)

#* Create the text box for displaying search results
results_text = tk.Text(window, height=10, width=50)
results_text.grid(row=4, column=0, columnspan=2, padx=10)

if __name__ == '__main__':
    window.mainloop()
