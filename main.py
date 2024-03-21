
# main.py

# Import the necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import sqlite3

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def dashboard():
    # Get the system performance data
    conn = sqlite3.connect('system_performance.db')
    df = pd.read_sql_query("SELECT * FROM system_performance", conn)
    conn.close()

    # Render the dashboard template
    return render_template('dashboard.html', data=df.to_dict())

@app.route('/errors')
def errors():
    # Get the error logs
    conn = sqlite3.connect('error_logs.db')
    df = pd.read_sql_query("SELECT * FROM error_logs", conn)
    conn.close()

    # Render the errors template
    return render_template('errors.html', data=df.to_dict())

@app.route('/troubleshoot')
def troubleshoot():
    # Render the troubleshoot template
    return render_template('troubleshoot.html')

# Start the application
if __name__ == '__main__':
    app.run()
