import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('feedback.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    feedback TEXT NOT NULL
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to submit feedback
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END)

    if name and email and feedback:
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")

# Function to retrieve feedback
def retrieve_feedback():
    password = entry_password.get()
    
    # Hardcoded password (you can change this)
    if password == "admin123":
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()
        conn.close()
        
        feedback_output = "\n".join([f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Feedback: {row[3]}" for row in rows])
        
        # Display feedback in a messagebox
        if feedback_output:
            print("Feedback Entries", feedback_output)
        else:
            print("Feedback Entries", "No feedback entries found.")
    else:
        print("Access Denied", "Incorrect password!")

# Create main window
root = tk.Tk()
root.title("Customer Feedback")

# Create input fields for feedback
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Feedback").pack()
entry_feedback = tk.Text(root, height=5, width=30)
entry_feedback.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack()

# Create input field for password retrieval
tk.Label(root, text="Enter Password to Retrieve Feedback").pack()
entry_password = tk.Entry(root, show="*")  # Hide password input
entry_password.pack()

# Add retrieve button
retrieve_button = tk.Button(root, text="Retrieve Feedback", command=retrieve_feedback)
retrieve_button.pack()

# Run the application
root.mainloop()