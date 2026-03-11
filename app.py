from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <h1>CI/CD Docker Application</h1>
    <h2>Student Name: Jatin Nath</h2>
    <h2>Roll Number: 2023BCD0014</h2>
    <h2>Register Number: 2023BCD0014</h2>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)