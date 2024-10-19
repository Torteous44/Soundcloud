# main.py
import os
from download import download_soundcloud_track
from trim import trim_audio
from shazam import submit_to_audd
from utils import configure_logging, load_environment_variables

def main():
    # Configure logging and load environment variables
    configure_logging()
    load_environment_variables()

    # Prompt the user to input a SoundCloud URL
    soundcloud_url = input("Please enter the SoundCloud track URL: ").strip()

    # Validate if the URL is not empty
    if not soundcloud_url:
        print("Error: No URL provided. Exiting.")
        return

    # Start the download process
    downloaded_file = download_soundcloud_track(soundcloud_url)

    if downloaded_file and os.path.isfile(downloaded_file):
        # Trim the downloaded file
        trimmed_file = trim_audio(downloaded_file, downloaded_file.replace(".mp3", "_trimmed.mp3"), duration=10)
        if trimmed_file:
            # Identify the song using Audd.io
            song_data = submit_to_audd(trimmed_file)
            if song_data:
                # Extract and print song details
                result = song_data.get('result', {})
                track = result.get('title', 'Unknown')
                artist = result.get('artist', 'Unknown Artist')
                album = result.get('album', 'Unknown Album')
                release_date = result.get('release_date', 'Unknown Release Date')
                song_link = result.get('song_link', 'No Link Available')
                lyrics = result.get('lyrics', {}).get('lyrics', 'No lyrics available')

                print(f"\n--- Song Details ---")
                print(f"Title       : {track}")
                print(f"Artist      : {artist}")
                print(f"Album       : {album}")
                print(f"Release Date: {release_date}")
                print(f"Song Link   : {song_link}")

                # Print the lyrics, if available
                print("\n--- Lyrics ---")
                print(lyrics)
            else:
                print("Failed to identify the song.")
        else:
            print("Error trimming the audio.")
    else:
        print("Download was not successful. Exiting.")

if __name__ == "__main__":
    main()
