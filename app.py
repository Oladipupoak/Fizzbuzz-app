from flask import Flask, render_template, request
import random
app = Flask(__name__)
#The app should have one route, /fizzbuzz, that renders an HTML template.
# In the template, loop through the numbers 1 to 100 inside of an unordered list.
# For every number that is divisible by 3, show a list element with the word 'Fizz'
# For every number that is divisible by 5, show a list element with the word 'Buzz'
# For every number that is divisible by both 3 and 5, show a list element with 'FizzBuzz'
# For every other number, show a list element with the number
@app.get("/fizzbuzz")
def fizzbuzz_app():
    return render_template("index.html")
