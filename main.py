import streamlit as st

def main():
    st.title("Study Material Website")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Subjects"])

    if page == "Home":
        display_home_page()
    elif page == "About":
        display_about_page()
    elif page == "Subjects":
        display_subjects_page()

def display_home_page():
    st.header("Welcome to Our Study Material Website")
    st.write("Browse through different subjects to find study materials.")

def display_about_page():
    st.header("About Us")
    st.write("We are dedicated to providing high-quality study materials for various subjects.")

def display_subjects_page():
    st.header("Subjects")
    subjects = {
        "Python": "python.pdf",
        "Java": "java.pdf",
        "Machine Learning": "ml.pdf"
    }

    selected_subject = st.selectbox("Select a subject", list(subjects.keys()))

    if selected_subject in subjects:
        pdf_file = subjects[selected_subject]
        display_pdf(pdf_file)

def display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
    st.write(f"Viewing {pdf_file}")
    st.write("You can download the PDF file from the link below:")
    st.markdown(get_pdf_download_link(pdf_bytes, pdf_file), unsafe_allow_html=True)

def get_pdf_download_link(pdf_bytes, pdf_file):
    href = f'<a href="data:application/octet-stream;base64,{b64encode(pdf_bytes).decode()}" download="{pdf_file}">Download PDF</a>'
    return href

# Embedding HTML and CSS for styling
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f6;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        .sidebar .sidebar-content {
            background-color: #333;
            color: #fff;
        }
        .sidebar .title {
            color: #fff;
        }
        .container {
            padding: 20px;
        }
        .subject-select {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
        }
        .pdf-link {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            text-align: center;
            display: block;
            width: 200px;
            margin: auto;
            border-radius: 5px;
        }
        .pdf-link:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
