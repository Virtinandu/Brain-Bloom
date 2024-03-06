import streamlit as st
import PyPDF2

# Title and brief description
st.title("PDF Uploader")
st.write("Upload a PDF file to view its content.")

# File uploader
pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

if pdf_file is not None:
    # Read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Display the number of pages
    st.write(f"Number of pages: {pdf_reader.numPages}")

    # Display the text content of each page
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        st.write(f"Page {page_num + 1} content:")
        st.write(page.extractText())

st.markdown(
    """
        # Custom CSS and HTML styling
custom_css = 
<style>
body {
    font-family: Arial, sans-serif;
}
.container {
    max-width: 800px;
    margin: auto;
}
</style>

(custom_css, unsafe_allow_html=True)

container = st.container()
with container:
    # Your existing code
        """)