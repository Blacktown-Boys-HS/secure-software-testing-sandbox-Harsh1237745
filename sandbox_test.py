# Sandbox Testing Example
# Author: Harsh

# Simple login function
def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False


# ----------------------
# TEST CASES
# ----------------------

print("=== Normal Test ===")
print(login("admin", "1234"))   # Expected: True

print("\n=== Wrong Password ===")
print(login("admin", "wrong"))  # Expected: False

print("\n=== Empty Input ===")
print(login("", ""))            # Edge case

print("\n=== SQL Injection Attempt ===")
print(login("admin", "' OR 1=1"))  # Security test

print("\n=== Long Input ===")
print(login("A"*1000, "1234"))  # Stress test

print("\n=== None Input ===")
print(login(None, None))        # Error handling test
