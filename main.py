import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Study Material", page_icon=":books:", layout="wide")

# Add a CSS file to style the app
st.markdown("""
<style>
.big-font {
    font-size: 30px;
    color: #3F84B3;
}
.card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    border-radius: 5px;
    margin: 10px;
    padding: 10px;
}
.card:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Add study material as markdown links
st.write("<h1 class='big-font'>Study Material</h1>", unsafe_allow_html=True)
st.write("<a class='card' href='https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357332/' target='_blank'>Python Cookbook</a>", unsafe_allow_html=True)
st.write("<a class='card' href='https://automatetheboringstuff.com/' target='_blank'>Automate the Boring Stuff</a>", unsafe_allow_html=True)
st.write("<a class='card' href='https://docs.scipy.org/doc/numpy/reference/' target='_blank'>NumPy Reference</a>", unsafe_allow_html=True)
st.write("<a class='card' href='https://pandas.pydata.org/docs/' target='_blank'>Pandas Documentation</a>", unsafe_allow_html=True)
st.write("<a class='card' href='https://matplotlib.org/stable/contents.html' target='_blank'>Matplotlib Documentation</a>", unsafe_allow_html=True)