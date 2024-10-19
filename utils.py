# utils.py
from dotenv import load_dotenv
import logging
import os

def configure_logging():
    logging.basicConfig(
        filename='download.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def load_environment_variables():
    load_dotenv()

# Call load_environment_variables() from main.py before using the API key.
