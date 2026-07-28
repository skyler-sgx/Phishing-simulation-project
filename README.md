# Phishing Awareness Simulator
A lightweight desktop application built with **Python** and **Tkinter** that simulates a phishing login page for **educational and security awareness purposes**. The goal is to help users experience and recognize common phishing tactics in a safe, controlled environment — with no real data ever being transmitted externally.

# Overview
Phishing remains one of the most common and effective cyberattack vectors. This project demonstrates how a fake login page can be designed to mimic legitimate services, and then immediately educates the user on the red flags they may have missed — turning a simulated attack into a learning opportunity.
When a user enters credentials into the simulated "HackerMail" login form, the app:
1. Logs the submission locally (for training/demo purposes only)
2. Redirects to an **awareness screen** explaining that it was a simulation
3. Highlights the red flags present in the fake page
4. Provides actionable tips to protect against real phishing attempts

# Features
-  **Realistic fake login UI** — mimics common phishing page design patterns (urgency banners, fake security alerts, branded look)
-  **Red flag breakdown** — explains exactly which elements were designed to deceive
-  **Protection tips** — practical steps to avoid falling for real phishing attempts
-  **Local CSV logging** — records simulated submissions with timestamps for review/training reports
-  **Reset flow** — allows users to try again and reinforce learning
-  **Clear disclaimers** — the page states upfront that it is a simulated training tool

# Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.x |
| GUI Framework | Tkinter |
| Data Logging | CSV (built-in `csv` module) |
| Timestamps | `datetime` module |

# Project Structure
```
phishing-awareness-simulator/
│
├── main.py              # Application entry point
├── submissions.csv      # Auto-generated log file (created on first run)
└── README.md            # Project documentation
```

# Prerequisites
- Python 3.7 or higher
- Tkinter (included by default with most Python installations)

# Installation
```bash
git clone https://github.com/<your-username>/phishing-awareness-simulator.git
cd phishing-awareness-simulator
python main.py
```

# How It Works
1. **Launch the app** — a fake "HackerMail" sign-in page opens
2. **Enter any email/password** — the form accepts any input (no validation against real accounts)
3. **Submit** — the app logs the entry locally and reveals the awareness screen
4. **Review** — read through the red flags and protection tips
5. **Try again** — reset the simulation to reinforce the lesson

# Disclaimer
This project is intended **strictly for educational and security awareness purposes**, such as:
- Internal corporate security training
- Cybersecurity workshops and demos
- Academic projects on social engineering
It does **not** transmit any data externally — all submissions are stored locally in `submissions.csv` for review purposes only. Do not deploy this project to impersonate real services, target real users without consent, or use it in any unauthorized or malicious manner.
Using this tool against individuals without their informed consent may violate computer misuse, data protection, or anti-phishing laws depending on your jurisdiction.

# Use Cases
- Corporate security awareness training sessions
- Cybersecurity/InfoSec student demonstrations
- Portfolio project showcasing social engineering awareness
- Workshops on identifying phishing red flags

# Author
Shivani Gupta


