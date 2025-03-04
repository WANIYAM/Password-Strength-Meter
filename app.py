import streamlit as st
import re
import random

# List of common weak passwords
blacklist = {"password", "123456", "qwerty", "abc123", "password123", "letmein", "welcome"}

# Function to generate a strong password
def generate_strong_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(12))

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Blacklist Check
    if password.lower() in blacklist:
        feedback.append("❌ This password is too common. Choose a more secure one.")
        return 1, feedback

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Strength Rating
        if score == 4:
            st.success("✅ Strong Password! Great job!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for msg in feedback:
                st.write(msg)
            st.info(f"🔹 Try using this strong password: `{generate_strong_password()}`")
    else:
        st.warning("⚠️ Please enter a password!")

