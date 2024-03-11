import requests

# The base URL of the server
BASE_URL = 'http://example.com'

# Create a session object, which will be used to maintain cookies across requests
session = requests.Session()

# Data to be sent for login
login_data = {
    'username': 'your_username',
    'password': 'your_password'
}

# Login request
login_response = session.post(f'{BASE_URL}/login', data=login_data)

# Check if login was successful
if login_response.ok:
    print("Logged in successfully!")

    # Now that the session is established, we can access protected endpoints
    protected_response = session.get(f'{BASE_URL}/protected')

    if protected_response.ok:
        print("Accessed protected content:", protected_response.text)
    else:
        print("Failed to access protected content:", protected_response.status_code)

    # Logout to end the session
    logout_response = session.get(f'{BASE_URL}/logout')
    if logout_response.ok:
        print("Logged out successfully!")
    else:
        print("Failed to log out:", logout_response.status_code)

else:
    print("Login failed:", login_response.status_code)