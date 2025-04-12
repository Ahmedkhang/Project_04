import hashlib

# Modify the hashed_password function to accept a password parameter
def hashed_password(password):  # Accept a password as an argument
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(stored_logins, email, password):
    """Checks if the hashed password matches the stored password hash."""
    return stored_logins.get(email) == hashed_password(password)  # Compare the hashed password

def main():
    # Store the hashed passwords in a dictionary
    stored_logins = {
        "user1@example.com": hashed_password("user1123"),  # Corrected call with password argument
        "user2@gmail.com": hashed_password("user2123"),
        "admin@site.com": hashed_password("admin123")
    }

    # Test login functionality
    print(login(stored_logins, "user1@example.com", "user1123"))  
    print(login(stored_logins, "user1@example.com", "wrongpassword")) 
    print(login(stored_logins, "admin@site.com", "admin123"))  
    print(login(stored_logins, "unknown@xyz.com", "mypassword123")) 

if __name__ == '__main__':
    main()
