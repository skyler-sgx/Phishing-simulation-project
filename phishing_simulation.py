import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
LOG_FILE = "submissions.csv"
def log_submission(email, password):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "email", "password"])
        writer.writerow([datetime.now().isoformat(), email, password])
def handle_login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showwarning("Missing info", "Please fill both fields.")
        return
    log_submission(email, password)
    show_awareness_screen()
def show_awareness_screen():
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg="#f4f6f9")
    tk.Label(root, text="This was a phishing simulation!",
             font=("Segoe UI", 15, "bold"), bg="#f4f6f9", fg="#1e3c72").pack(pady=(25, 10))
    intro = ("You just experienced what a phishing attempt looks like.\n"
             "'HackerMail' is not a real service - this was built only\n"
             "to demonstrate how easily these attacks work.")
    tk.Label(root, text=intro, font=("Segoe UI", 10), bg="#f4f6f9", justify="left").pack(pady=(0, 15))
    red_flags = (
        "Red flags you may have missed:\n"
        "- Urgency & fear ('unusual sign-in activity' warning)\n"
        "- Generic greeting instead of your real name\n"
        "- Unfamiliar/unverified sender or domain\n"
        "- Being asked to 're-verify' your password from a link\n"
        "- A padlock/HTTPS icon alone doesn't guarantee safety\n"
    )
    tk.Label(root, text=red_flags, font=("Segoe UI", 10), bg="#f4f6f9",
             justify="left", anchor="w").pack(padx=30, pady=(0, 15), fill="x")
    protect = (
        "How to protect yourself:\n"
        "* Check the sender's actual email address\n"
        "* Hover over links before clicking\n"
        "* Never enter credentials via an email link, visit the site directly\n"
        "* Turn on multi-factor authentication (MFA)\n"
    )
    tk.Label(root, text=protect, font=("Segoe UI", 10), bg="#f4f6f9",
             justify="left", anchor="w").pack(padx=30, pady=(0, 20), fill="x")
    tk.Button(root, text="Try again", font=("Segoe UI", 10), bg="#2a5298", fg="white",
              command=build_login_screen).pack(pady=10)
def build_login_screen():
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg="#2a5298")
    global email_entry, password_entry
    frame = tk.Frame(root, bg="white", padx=30, pady=30)
    frame.pack(pady=40)
    tk.Label(frame, text="HackerMail", font=("Segoe UI", 16, "bold"),
             bg="white", fg="#1e3c72").pack()
    tk.Label(frame, text="Sign in to continue to your inbox", font=("Segoe UI", 9),
             bg="white", fg="#555").pack(pady=(0, 10))
    tk.Label(frame, text="Unusual sign-in activity detected.\nPlease verify your account immediately.",
             font=("Segoe UI", 8), bg="#fff4e5", fg="#8a5300", justify="left",
             padx=8, pady=6).pack(fill="x", pady=(0, 10))
    tk.Label(frame, text="Email address", font=("Segoe UI", 9), bg="white", anchor="w").pack(fill="x")
    email_entry = tk.Entry(frame, width=30)
    email_entry.pack(pady=(0, 8))
    tk.Label(frame, text="Password", font=("Segoe UI", 9), bg="white", anchor="w").pack(fill="x")
    password_entry = tk.Entry(frame, width=30, show="*")
    password_entry.pack(pady=(0, 12))
    tk.Button(frame, text="Verify Account", font=("Segoe UI", 10), bg="#2a5298", fg="white",
              command=handle_login).pack(fill="x")
    tk.Label(frame, text="(Simulated training page - no real data is transmitted)",
             font=("Segoe UI", 7), bg="white", fg="#999").pack(pady=(10, 0))
root = tk.Tk()
root.title("HackerMail - Sign In")
root.geometry("400x480")
root.resizable(False, False)
build_login_screen()
root.mainloop()