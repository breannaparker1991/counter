from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

if __name__ == "__main__":
    app.run(debug=True)
