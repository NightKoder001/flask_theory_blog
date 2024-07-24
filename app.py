from flask import Flask
from config import Config

# Create a Flask application instance
app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, Flask!'

# Check if the script is run directly
if __name__ == "__main__":
    app.run(debug=True)
