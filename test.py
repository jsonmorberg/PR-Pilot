import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Fetch GitHub token from environment variable
token = os.getenv('GITHUB_TOKEN')

if token:
    print(f"GitHub Token loaded successfully: {token[:4]}...")  # Print part of the token to confirm
else:
    print("GitHub Token not found!")
