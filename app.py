from flask import Flask


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generatefile", methods=['GET'])
def generate_file():
    filepath = 'genefile.txt'
    content = "this is generage ifle"
    with open(filepath, 'w') as file:
        file.write(content)
    return "<p>file generated successfully</p>"

if __name__ == "__main__":
    app.run() 