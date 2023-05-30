from CTFdPy.csv import CSVHandler
from CTFdPy.client import Client

API_KEY = "f976c2756984558face3245bfcc92ab6dba4fe3c10c2533d2a1dbb6fbfb0d639"
URL = "http://test.gryphons.sg/"
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