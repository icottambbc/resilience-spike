from flask import Flask, render_template
import numpy as np
app = Flask(__name__)

def sum():
  DATA = [10, 9, 4, 15, 2, 9, 13, 10, 8, 8, 22, 6, 3, 8, 4, 12, 5, 9, 12]
  return str(np.sum(DATA))

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/calculation")
def about():
  return sum()


if __name__ == '__main__':
  app.run()

# the plan
# 1) Return a button
# 2) When you click the button, it should run a program that generates an array with 1000 elements and then sums them. It returns the summed value on a new page (need to pass the values to the new page)