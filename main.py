from flask import Flask, render_template, send_from_directory

main= Flask(__name__)

# Define the list of subjects with their associated PDF files
subjects = {
    'Python': 'python Unit 1.pdf',
    'Java': 'java.pdf',
    'Machine Learning': 'machine_learning.pdf'
}

@main.route('/')
def index():
    return render_template('index.html', subjects=subjects)

@main.route('/subjects/<filename>')
def download_subject(filename):
    return send_from_directory('pdfs', filename)

if __name__ == '__main__':
    main.run(debug=True)
