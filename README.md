## 🔐 Password Strength Checker

A simple Python-based project that checks the strength of a password based on multiple security rules and provides suggestions to improve it.

---

# 🚀 Features
- ✅ Checks password length
- ✅ Detects:
- Uppercase letters
- Lowercase letters
- Digits
- Special characters
-  ✅ Calculates password strength:
    - Weak
    - Medium
    - Strong
- ✅ Provides suggestions to improve password security

---

🧠 How It Works

- The program evaluates the password using a scoring system:
- Length ≥ 8 → +1 score
- Length ≥ 12 → +1 score
- Contains uppercase → +1
- Contains lowercase → +1
- Contains digits → +1
- Contains special characters → +1
# 🔎 Strength Criteria:
- 0–2 → Weak Password
- 3–4 → Medium Password
- 5–6 → Strong Password

---

# 📥 Input

User enters a password through the terminal:

Enter Password: your_password_here
# 📤 Output Example
Medium Password

Suggestions to improve:
- Increase length to at least 8 characters
- Add special characters
  
  ---

# 🛠️ Technologies Used
- Python 🐍
- Basic string methods (isupper(), islower(), isdigit())

---

# 💡 Future Improvements
- Add GUI using Tkinter 🎨
- Add real-time strength meter 🔋
- Add password blacklist (common passwords)
- Integrate with web app 🌐

---

# 👨‍💻 Author

Aum Lakhani
