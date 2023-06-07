from flask import Flask, render_template


from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return 'Hello World!'


@app.route('/dojo') 
def dojo():
    return 'Dojo!'


@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    if name.isdigit(): # The isdigit() method returns True if all the characters are digits, otherwise False.
        return "Please enter a string!"
    else:
        return "Hi " + name.capitalize() + "!"


@app.route('/repeat/<num>/<word>') 
def repeat(num, word):
    if isinstance(num, int) and isinstance(word, str):
        return f"{word}<br>" * num
    else:
        return "404! No Response!" 


@app.errorhandler(404)
def notFound(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
