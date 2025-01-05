from flask import render_template
import os
import config

from models import Trail  # Importing the Trail model
API_BASE_URL = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"

# Initialize Connexion app
connex_app = config.connex_app
app = connex_app.app  # Access the underlying Flask app
config.db.init_app(app)  # Bind the db instance to the Flask app
config.ma.init_app(app)  # Bind the ma instance to the Flask app

# Add the API documentation from swagger.yml
connex_app.add_api(os.path.join(config.basedir, "swagger.yml"))

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
    connex_app.run(host="0.0.0.0", port=8000, debug=True)

@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user by calling the external Auth API.
    """
    # Get email and password from the request
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Call the external Auth API
    try:
        response = requests.post(f"{API_BASE_URL}/login", json={"username": email, "password": password})
        if response.status_code == 200:
            # Return the token to the user
            return jsonify(response.json()), 200
        else:
            # Return any error messages from the Auth API
            return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to connect to the Auth API", "details": str(e)}), 500