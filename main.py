import streamlit as st
from PyPDF2 import PdfFileReader
import streamlit_option_menu as st_option_menu

# Set page title and favicon
st.set_page_config(page_title="Study Material", page_icon=":books:", layout="wide")

# Add a CSS file to style the app
st.markdown("""
<style>
.big-font {
    font-size: 30px;
    color: #3F84B3;
}
.sidebar {
    background-color: #F2F2F2;
    padding: 10px;
    border-radius: 5px;
}
.pdf-container {
    border: 1px solid #CCCCCC;
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
    height: 80vh;
    overflow-y: scroll;
}
</style>
""", unsafe_allow_html=True)

# Add sidebar with options
selected_chapter = st_option_menu.sidebar("Chapters", ["Chapter 1", "Chapter 2", "Chapter 3"], index=0)

# Load PDF and display selected chapter
pdf_path = "path/to/your/pdf/study_material.pdf"
pdf = PdfFileReader(open(pdf_path, "rb"))
num_pages = pdf.getNumPages()

for i in range(num_pages):
    page = pdf.getPage(i)
    if i == 0 and selected_chapter != "Chapter 1":
        continue
    elif i == num_pages - 1 and selected_chapter == "Chapter 3":
        break
    elif i >= num_pages - 1 or i < (pdf.getPage(num_pages - 1).extractText().split(" ")).index(selected_chapter):
        st.sidebar.write(f"Page {i+1}")
        st.sidebar.markdown(page.extractText(), unsafe_allow_html=True)
        st.markdown("""
        <div class="pdf-container">
            {}
        </div>
        """.format(page.extractText()), unsafe_allow_html=True)