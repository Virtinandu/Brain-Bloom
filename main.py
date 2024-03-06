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
    st.header("Welcome to Brain Bloom")
    st.header_alignment=('center')
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
"""
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body{
  background-image: url("data:image/jpeg;base64,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");

  background-repeat: no-repeat;
  background-size: 1400px 700px;

}

::selection{
    color: #eff;
    background: #007bff;
}

.start_btn,{
  position: absolute;
  transform: translate(-50%, -50%);
  box-shadow: 0 30px 8px 0 rgba(0, 0, 0, 0.2),
              0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.info_box,
.quiz_box,
.result_box{
    position: absolute;
    top: 50%;
    left: 50%;
    width: 600px;
    transform: translate(-50%, -50%);
    box-shadow: 0 3px 8px 0 rgba(0, 0, 0, 0.2),
                0 6px 20px 0 rgba(0, 0, 0, 0.9);
}

.info_box.activeInfo,
.quiz_box.activeQuiz,
.result_box.activeResult{
    opacity: 1;
    z-index: 5;
    pointer-events: auto;
    transform: translate(-50%, -50%) scale(1);
}

.start_btn button{
    font-size: 25px;
    font-weight: 500;
    color: #fff;
    padding: 15px 30px;
    outline: none;
    border: none;
    border-radius: 5px;
    background: #02751D;
    cursor: pointer;
    margin-left: 600px;
    /* margin-bottom: 400px; */
    margin-top: 30px;
    /* top: 40px; */
}

.start_btn button:hover {background-color: #129609}

 .start_btn:active {
  box-shadow: 0 1px #666;
}

.info_box{
    width: 650px;
    height: 500px;
    background: #FCF29F;
    border-radius: 5px;
    transform: translate(-50%, -50%) scale(0.9);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
}

.info_box .info-title{
    height: 70px;
    margin-top: 17px;
    width: 100%;
    border-bottom: 2px solid darkgrey;
    display: flex;
    align-items: center;
    padding: 0 30px;
    border-radius: 5px 5px 0 0;
    font-size: 30px;
    font-weight: 600;
}

.info_box .info-list{
    padding: 25px 40px;
}

.info_box .info-list .info{
    margin: 20px 10px;
    font-size: 20px;
}

.info_box .info-list .info span{
    font-weight: 600;
    color: #007bff;
}
.info_box .buttons{
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 30px;
    border-top: 2px solid grey;
}

.info_box .buttons button{
    margin: 0 5px;
    margin-top: 35px;
    height: 40px;
    width: 100px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    border: none;
    outline: none;
    border-radius: 5px;
    border: 1px solid #5F3BE3;
    transition: all 0.3s ease;
}

.quiz_box{
    height: 450px;
    width: 550px;
    background: #FFAB7A;
    border-radius: 5px;
    transform: translate(-50%, -50%) scale(0.9);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
    /* height: 500px; */
}

.quiz_box header{
    position: relative;
    z-index: 2;
    height: 90px;
    padding: 0 30px;
    background: #CF2B5C;
    border-radius: 5px 5px 0 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0px 3px 5px 1px rgba(0,0,0,0.1);
    border-color: grey;
}

.quiz_box header .title{
    font-size: 30px;
    background-color:#CF2B5C;
    font-weight: 600;
    color: white;
}

.quiz_box header .timer{
    color: #004085;
    background: #cce5ff;
    border: 1px solid #b8daff;
    height: 45px;
    padding: 0 8px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 145px;
}

.quiz_box header .timer .time_left_txt{
    font-weight: 410;
    font-size: 17px;
    user-select: none;
}

.quiz_box header .timer .timer_sec{
    font-size: 18px;
    font-weight: 500;
    height: 30px;
    width: 45px;
    color: #fff;
    border-radius: 5px;
    line-height: 30px;
    text-align: center;
    background: #343a40;
    border: 1px solid #343a40;
    user-select: none;
}

.quiz_box header .time_line{
    position: absolute;
    bottom: 0px;
    /* width: 200px; */
    right: 0px;
    left: 0px;
    height: 3px;
    background: #007bff;
}

section{
    height: 350px;
    padding: 25px 30px 20px 30px;
    background: #fff;
}

section .que_text{
    font-size: 25px;
    font-weight: 600;
}

section .option_list{
    padding: 20px 0px;
    display: block;
}

section .option_list .option{
    background: aliceblue;
    border: 1px solid #84c5fe;
    border-radius: 5px;
    padding: 8px 15px;
    font-size: 17px;
    margin-bottom: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

section .option_list .option:last-child{
    margin-bottom: 0px;
}

section .option_list .option:hover{
    color: #004085;
    background: #cce5ff;
    border: 1px solid #b8daff;
}

section .option_list .option.correct{
    color: #155724;
    background: #d4edda;
    border: 1px solid #c3e6cb;
}

section .option_list .option.incorrect{
    color: #721c24;
    background: #f8d7da;
    border: 1px solid #f5c6cb;
}

section .option_list .option.disabled{
    pointer-events: none;
}

section .option_list .option .icon{
    height: 26px;
    width: 26px;
    border: 2px solid transparent;
    border-radius: 50%;
    text-align: center;
    font-size: 13px;
    pointer-events: none;
    transition: all 0.3s ease;
    line-height: 24px;
}
.option_list .option .icon.tick{
    color: #23903c;
    border-color: #23903c;
    background: #d4edda;
}

.option_list .option .icon.cross{
    color: #a42834;
    background: #f8d7da;
    border-color: #a42834;
}

footer{
    height: 80px;
    padding: 0 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid gray;
    background: #BAB3AF;
}

footer .total_que span{
    display: flex;
    user-select: none;
}

footer .total_que span p{
    font-weight: 500;
    padding: 0 5px;
}

footer .total_que span p:first-child{
    padding-left: 0px;
}

footer button{
    height: 40px;
    padding: 0 13px;
    font-size: 18px;
    font-weight: 400;
    cursor: pointer;
    border: none;
    outline: none;
    color: #fff;
    border-radius: 5px;
    background: #007bff;
    border: 1px solid #007bff;
    line-height: 10px;
    opacity: 0;
    pointer-events: none;
    transform: scale(0.95);
    transition: all 0.3s ease;
}

footer button:hover{
    background: #90F0F0;
    color: black;
}

footer button.show{
    opacity: 1;
    pointer-events: auto;
    transform: scale(1);
}

.result_box{
    background: #FCC2C3;
    border-radius: 5px;
    /* border-style: solid pink; */
    display: flex;
    padding: 25px 30px;
    width: 550px;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    transform: translate(-50%, -50%) scale(0.9);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
}

.result_box .icon{
    font-size: 100px;
    color: #007bff;
    margin-bottom: 10px;
}

.result_box .complete_text{
    font-size: 20px;
    font-weight: 500;
}

.result_box .score_text span{
    display: flex;
    margin: 10px 0;
    font-size: 18px;
    font-weight: 500;
}

.result_box .score_text span p{
    padding: 0 4px;
    font-weight: 600;
}

.result_box .buttons{
    display: flex;
    margin: 20px 0;
}

.result_box .buttons button{
    margin: 0 10px;
    height: 45px;
    padding: 0 20px;
    font-size: 18px;
    font-weight: 500;
    cursor: pointer;
    border: none;
    outline: none;
    border-radius: 5px;
    border: 1px solid #007bff;
    transition: all 0.3s ease;
}

.buttons button.restart{
    color: #fff;
    background: #007bff;
}

.buttons button.restart:hover{
    background: #0263ca;
}

.buttons button.quit{
    color: #007bff;
    background: #fff;
}

.buttons button.quit:hover{
    color: #fff;
    background: #007bff;
}
"""
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }

        header {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
        }

        nav {
            background-color: #666;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        main {
            padding: 20px;
        }

        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Simple Website</h1>
    </header>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
    <main>
        <h2>About Us</h2>
        <p>This is a simple website created using HTML and CSS.</p>
        <p>Feel free to explore!</p>
    </main>
    <footer>
        <p>&copy; 2024 Simple Website. All rights reserved.</p>
    </footer>
</body>
</html>"""
if __name__ == "__main__":
    main(),
unsafe_allow_html=True
