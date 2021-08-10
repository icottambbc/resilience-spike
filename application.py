from flask import Flask, render_template
from random import randrange
import numpy as np
app = Flask(__name__)

def sum():
  DATA = []
  for i in range(1000000):
    DATA.append(randrange(10))
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