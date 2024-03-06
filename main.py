import streamlit as st

def main():
    st.title("Welcome to Our Website")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

    if page == "Home":
        display_home_page()
    elif page == "About":
        display_about_page()
    elif page == "Contact":
        display_contact_page()

def display_home_page():
    st.header("Home Page")
    st.write("This is the home page of our website.")
    st.image("https://via.placeholder.com/500", caption="Home Page Image")

def display_about_page():
    st.header("About Us")
    st.write("We are a team of developers creating awesome web applications.")
    st.image("https://via.placeholder.com/500", caption="About Us Image")

def display_contact_page():
    st.header("Contact Us")
    st.write("You can reach out to us via email: contact@example.com")

# Adding some basic styling
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

if __name__ == "__main__":
    main()
