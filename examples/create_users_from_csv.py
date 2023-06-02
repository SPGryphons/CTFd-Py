from CTFdPy.csv import CSVHandler
from CTFdPy.client import Client

API_KEY = "<YOUR_API_KEY>"
URL = "<YOUR_CTFD_URL>"
client = Client(API_KEY, URL)

# Example user creation
handler = CSVHandler('users.csv')
users = handler.read_csv()

for user in users:
    try:
        res = client.create_user(**user)
        
        print(res['password'])
        # You can store the password elsewhere, safely.
    except Exception as e:
        print(f"Error creating user '{user['username']}': {str(e)}")
