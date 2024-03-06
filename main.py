import streamlit as st

def main():
    # Sidebar options
    st.sidebar.title("Index")
    page = st.sidebar.selectbox("Select a page", ["Home", "Subjects", "About"])

    if page == "Home":
        display_home_page()
    elif page == "Subjects":
        display_subjects_page()
    elif page == "About":
        display_about_page()

def display_home_page():
    st.header("Welcome to our Study Material Website")

def display_subjects_page():
    st.header("Subjects")
    subjects = ["Python", "Android", "Java", "Computer Networks"]

    selected_subject = st.selectbox("Select a subject", subjects)

    if selected_subject == "Python":
        display_Python_material()
    elif selected_subject == "Android":
        display_Android_material()
    elif selected_subject == "Java":
        display_Java_material()
    elif selected_subject == "Computer Networks":
        display_Computer_Networks_material()

def display_Python_material():
    st.subheader("Python Study Material")

def display_Android_material():
    st.subheader("Android Study Material")

def display_Java_material():
    st.subheader("Java Study Material")

def display_Computer_Networks_material():
    st.subheader("Computer Networks Study Material")

def display_about_page():
    st.header("About")
    st.write("This website is created using Streamlit, a popular Python library for building web apps.")

if __name__ == "__main__":
    main()

# Adding HTML and CSS styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #333;
            color: #fff;
        }
        .sidebar .title {
            color: #fff;
        }
        .st-bd {
            padding: 20px;
        }
        .st-df {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3, h4, h5, h6 {
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True
)
