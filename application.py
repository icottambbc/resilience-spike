from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/about")
def about():
    return "All about Flask"


if __name__ == '__main__':
  app.run()

# the plan
# 1) Return a button
# 2) When you click the button, it should run a program that generates an array with 1000 elements and then sums them. It returns the summed value