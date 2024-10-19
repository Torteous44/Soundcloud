# shazam.py
import os
import requests

# Audd.io API settings
AUDD_API_URL = "https://api.audd.io/recognize"
AUDD_API_KEY = os.getenv("AUDD_API_KEY")

def submit_to_audd(audio_file):
    """
    Submits the trimmed MP3 file to the Audd.io API for song identification.
    """
    try:
        # Prepare data payload hello
        data = {
            "api_token": AUDD_API_KEY,
            "return": "lyrics,apple_music,spotify"
        }

        # Prepare the file payload with correct 'file' key
        files = {
            "file": open(audio_file, "rb")
        }

        # Send POST request to Audd.io API
        response = requests.post(AUDD_API_URL, data=data, files=files)

        # Close the file after making the request
        files["file"].close()

        if response.status_code == 200:
            try:
                return response.json()  # Ensure correct JSON parsing
            except ValueError:
                print("Error parsing JSON response from Audd.io.")
                return None
        else:
            print(f"Failed to submit to Audd.io. Status Code: {response.status_code}")
            print(f"Response content: {response.content}")
            return None

    except Exception as e:
        print(f"Error submitting to Audd.io: {e}")
        return None
