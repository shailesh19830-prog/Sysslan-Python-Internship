import re # Regular Expression module

def validate_email(email):
    # Basic regex pattern for email: text@text.text
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

# Testing
test_email = "shailesh@example.com"
print(f"Email: {test_email} -> Valid? {validate_email(test_email)}")

test_email2 = "invalid-email.com"
print(f"Email: {test_email2} -> Valid? {validate_email(test_email2)}")