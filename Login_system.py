# 📨 Gmail credentials (for simulation only)
# These are just test credentials for demonstration
# Gmail: sami@gmail.com
# Password: 1234

# Ask the user to enter their email
email = input("Enter your email: ")

# Check if the email contains '@' to ensure it's a valid format
if "@" in email:
    # Ask for password only if the email format is valid
    password = input("Enter your password: ")

    # ✅ Case 1: Both email and password are correct
    if email == "sami@gmail.com" and password == "1234":
        print("✅ You logged in successfully!")

    # ❌ Case 2: Email is correct but password is incorrect
    elif email == "sami@gmail.com" and password != "1234":
        print("⚠️ Password incorrect")
        password = input("Enter your password again: ")

        # Check again if the second attempt is correct
        if password == "1234":
            print("🔓 Finally logged in successfully!")
        else:
            print("🚫 Again wrong password!")

    # 🚷 Case 3: Any other email or password combination
    else:
        print("❌ Wrong credentials. Try again.")

# ⚠️ Case 4: Invalid email format (missing '@')
else:
    print("📩 Email galat hai — sahi likho (Invalid email format)")