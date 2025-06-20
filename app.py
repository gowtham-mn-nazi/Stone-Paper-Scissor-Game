from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({
        'user': user_choice,
        'computer': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
