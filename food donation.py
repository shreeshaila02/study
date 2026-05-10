from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ----------------

def init_db():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS donations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_name TEXT,
        food_name TEXT,
        quantity TEXT,
        location TEXT,
        status TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# ---------------- HOME PAGE ----------------

@app.route('/')
def home():

    conn = sqlite3.connect('food.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM donations")
    donations = cur.fetchall()

    conn.close()

    html = '''
    <html>
    <head>
        <title>Food Donation System</title>
    </head>
    <body>

    <h1>Food Donation Management System</h1>

    <a href="/donate">Donate Food</a>
    <br><br>
    <a href="/ngo">NGO Dashboard</a>

    <h2>All Donations</h2>

    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th>
            <th>Donor</th>
            <th>Food</th>
            <th>Quantity</th>
            <th>Location</th>
            <th>Status</th>
        </tr>

        {% for row in donations %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
            <td>{{ row[5] }}</td>
        </tr>
        {% endfor %}

    </table>

    </body>
    </html>
    '''

    return render_template_string(html, donations=donations)

# ---------------- DONATE PAGE ----------------

@app.route('/donate', methods=['GET', 'POST'])
def donate():

    if request.method == 'POST':

        donor_name = request.form['donor_name']
        food_name = request.form['food_name']
        quantity = request.form['quantity']
        location = request.form['location']

        conn = sqlite3.connect('food.db')
        cur = conn.cursor()

        cur.execute('''
        INSERT INTO donations
        (donor_name, food_name, quantity, location, status)
        VALUES (?, ?, ?, ?, ?)
        ''', (donor_name, food_name, quantity, location, 'Available'))

        conn.commit()
        conn.close()

        return redirect('/')

    html = '''
    <html>
    <head>
        <title>Donate Food</title>
    </head>
    <body>

    <h1>Donate Food</h1>

    <form method="POST">

        <label>Donor Name:</label><br>
        <input type="text" name="donor_name" required>
        <br><br>

        <label>Food Name:</label><br>
        <input type="text" name="food_name" required>
        <br><br>

        <label>Quantity:</label><br>
        <input type="text" name="quantity" required>
        <br><br>

        <label>Location:</label><br>
        <input type="text" name="location" required>
        <br><br>

        <button type="submit">Donate</button>

    </form>

    <br>
    <a href="/">Back to Home</a>

    </body>
    </html>
    '''

    return render_template_string(html)

# ---------------- NGO DASHBOARD ----------------

@app.route('/ngo')
def ngo_dashboard():

    conn = sqlite3.connect('food.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM donations WHERE status='Available'")
    donations = cur.fetchall()

    conn.close()

    html = '''
    <html>
    <head>
        <title>NGO Dashboard</title>
    </head>
    <body>

    <h1>NGO Dashboard</h1>

    <table border="1" cellpadding="10">

    <tr>
        <th>ID</th>
        <th>Donor</th>
        <th>Food</th>
        <th>Quantity</th>
        <th>Location</th>
        <th>Action</th>
    </tr>

    {% for row in donations %}
    <tr>
        <td>{{ row[0] }}</td>
        <td>{{ row[1] }}</td>
        <td>{{ row[2] }}</td>
        <td>{{ row[3] }}</td>
        <td>{{ row[4] }}</td>

        <td>
            <a href="/accept/{{ row[0] }}">Accept</a>
        </td>
    </tr>
    {% endfor %}

    </table>

    <br>
    <a href="/">Back to Home</a>

    </body>
    </html>
    '''

    return render_template_string(html, donations=donations)

# ---------------- ACCEPT DONATION ----------------

@app.route('/accept/<int:id>')
def accept(id):

    conn = sqlite3.connect('food.db')
    cur = conn.cursor()

    cur.execute("UPDATE donations SET status='Accepted' WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/ngo')

# ---------------- RUN APP ----------------

if __name__ == '__main__':
    app.run(debug=True)