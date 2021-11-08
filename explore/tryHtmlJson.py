from flask import Flask, request, url_for, redirect, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')

@app.route('/get_current_user', methods=['GET', 'POST'])
def get_current_user():
    user = {'name': 'Alice', 'birth-year': 1986}
    return jsonify(user)

