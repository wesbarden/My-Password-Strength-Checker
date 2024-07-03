import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    # Password strength criteria
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Calculate strength score
    score = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    
    # Strength levels
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    # Suggestions for improvement
    suggestions = []
    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not digit_criteria:
        suggestions.append("Password should include at least one digit.")
    if not uppercase_criteria:
        suggestions.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Password should include at least one lowercase letter.")
    if not special_char_criteria:
        suggestions.append("Password should include at least one special character.")

    return strength_levels[score], suggestions

def check_password():
    password = password_entry.get()
    strength, suggestions = check_password_strength(password)
    
    result_label.config(text=f"Password Strength: {strength}")
    suggestions_text = "\n".join(suggestions)
    suggestions_label.config(text=suggestions_text)

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Password Strength: ")
result_label.pack(pady=5)

suggestions_label = tk.Label(root, text="", justify="left")
suggestions_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()




