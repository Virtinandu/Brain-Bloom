import streamlit as st

def main():

    # Sidebar options
    st.sidebar.title ("Index")
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
    subjects = ["Python", "Android", "Java", "Computer Netwroks"]

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
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creative Home Page</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #FFFFFF;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background-color: #FFFFFF;
            color: #fff;
            text-align: center;
            padding: 30px 0;
        }
        h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
            color: #555;
            margin-bottom: 30px;
        }
        .cta-button {
            display: inline-block;
            background-color: #ff6b6b;
            color: #fff;
            text-decoration: none;
            padding: 15px 30px;
            border-radius: 5px;
            font-size: 20px;
            transition: background-color 0.3s ease;
        }
        .cta-button:hover {
            background-color: #ff4f4f;
        }
        .features {
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
        }
        .feature {
            flex: 1;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .feature:hover {
            transform: translateY(-5px);
        }
        .feature h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .feature p {
            font-size: 16px;
            color: #777;
        }
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px 0;
            position: absolute;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Welcome to Our Website</h1>
            <p>We provide study materials</p>
            <a href="#" class="cta-button">Get Started</a>
        </div>
    </header>
    <div class="container">
        <div class="features">
            <div class="feature">
                <h2>Feature 1</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et enim non est fringilla venenatis quis in nulla.</p>
            </div>
            <div class="feature">
                <h2>Feature 2</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et enim non est fringilla venenatis quis in nulla.</p>
            </div>
            <div class="feature">
                <h2>Feature 3</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et enim non est fringilla venenatis quis in nulla.</p>
            </div>
        </div>
    </div>
    <footer>
        <p>&copy; 2024 Creative Website. All rights reserved.</p>
    </footer>
</body>
</html>
"""
if __name__ == "__main__":
    main()
st.write(html_code, unsafe_allow_html=True)

