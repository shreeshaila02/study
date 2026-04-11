from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simple HTML template for login
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Dummy check (replace with database validation)
        if username == "admin" and password == "1234":
            return redirect(url_for("success"))
        else:
            error = "Invalid credentials. Try again."
    return render_template_string(login_page, error=error)

@app.route("/success")
def success():
    return "<h1>Login Successful! 🎉</h1>"

if __name__ == "__main__":
    app.run(debug=True)