from dotenv import load_dotenv
import os

print("Config file is being executed")

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') # or 'default-secret-key'
    DATABASE_URL = os.environ.get('DATABASE_URL') # or 'sqlite:///mydatabase.db'
    # Add other configuration settings here
