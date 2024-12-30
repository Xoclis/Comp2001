from flask import Flask, render_template
import os
import config
from models import Trail  # Importing the Trail model

# Initialize Connexion app
app = config.connex_app

# Add the API documentation from swagger.yml
app.add_api(os.path.join(config.basedir, "swagger.yml"))

@app.route("/")
def home():
    try:
        # Query all trails from the database
        trails = Trail.query.all()
    except Exception as e:
        return f"An error occurred: {e}", 500
    
    # Pass the trails to the home.html template
    return render_template("home.html", trails=trails)

if __name__ == "__main__":
    # Run the application
    app.run(host="0.0.0.0", port=8000, debug=True)
