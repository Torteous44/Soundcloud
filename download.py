# download.py
import yt_dlp
import os
import logging

def download_soundcloud_track(track_url):
    """
    Downloads an audio track from SoundCloud using yt-dlp and saves it in MP3 format.
    """
    output_path = os.path.join(os.getcwd(), "downloaded_track")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': False,  # Set to False to get detailed download output
        'no_warnings': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logtostderr': True,
    }

    try:
        # Download the track from SoundCloud
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([track_url])
        
        downloaded_file_path = output_path + ".mp3"
        logging.info(f"Successfully downloaded: {track_url} as {downloaded_file_path}")
        
        if os.path.getsize(downloaded_file_path) > 0:
            return downloaded_file_path
        else:
            return None
    except yt_dlp.utils.DownloadError as de:
        logging.error(f"DownloadError: {de}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None
