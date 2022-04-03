from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'I love my dog!!!'

@app.route('/')
def main():
  if 'count' not in session:
    session["count"] = 0
  else:
    session['count'] += 1
  return render_template("index.html")

@app.route('/destroy')
def destroy():
  session.clear()
  # session.pop('counter') other way
  return redirect('/')

@app.route('/increase')
def increase():
  session['count'] += 2
  return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
