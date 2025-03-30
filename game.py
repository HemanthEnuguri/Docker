import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Global dictionary to store game state
game_state = {}

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Number Game</title>
  </head>
  <body>
    <h1>Welcome to the Guess the Number Game!</h1>
    <h3>{{ message }}</h3>

    {% if user_name %}
    <h3>Welcome, {{ user_name }}!</h3>
    <p>Guesses taken: {{ guesses_taken }}</p>

    <form method="POST">
      <label for="guess">Enter a guess between 1 and 100:</label>
      <input type="number" id="guess" name="guess" min="1" max="100" required>
      <button type="submit">Guess</button>
    </form>
    {% else %}
    <form method="GET">
      <label for="user_name">Enter your name: </label>
      <input type="text" id="user_name" name="user_name" required>
      <button type="submit">Start Game</button>
    </form>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize game state if it's the first time or if the game was reset
    if 'user_name' not in game_state:
        return render_template_string(TEMPLATE, message="Enter your name to start playing!", user_name="", guesses_taken=0)

    if request.method == "POST":
        try:
            user_guess = int(request.form['guess'])
            user_name = game_state.get('user_name', 'Guest')
            number_to_guess = game_state.get('number_to_guess', 0)
            guesses_taken = game_state.get('guesses_taken', 0)

            # Increment guesses taken
            guesses_taken += 1
            game_state['guesses_taken'] = guesses_taken

            if user_guess < number_to_guess:
                message = "Too low! Try again."
            elif user_guess > number_to_guess:
                message = "Too high! Try again."
            else:
                message = f"Congratulations, {user_name}! You guessed the number in {guesses_taken} tries."
                game_state.clear()  # Clear game state after winning
            return render_template_string(TEMPLATE, message=message, user_name=user_name, guesses_taken=guesses_taken)

        except ValueError:
            message = "Please enter a valid number."
            return render_template_string(TEMPLATE, message=message, user_name=game_state.get('user_name', 'Guest'), guesses_taken=game_state.get('guesses_taken', 0))

    # If the request is GET, ask for the user's name
    user_name = request.args.get('user_name', 'Guest')
    if user_name:
        game_state['user_name'] = user_name
        game_state['number_to_guess'] = random.randint(1, 100)
        game_state['guesses_taken'] = 0
        return render_template_string(TEMPLATE, message="Enter your guess!", user_name=user_name, guesses_taken=0)

if __name__ == "__main__":
    app.run(debug=True)
