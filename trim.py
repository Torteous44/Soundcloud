# trim.py
import subprocess

def trim_audio(input_file, output_file, start_time=0, duration=30):
    """
    Trims the downloaded audio file to the specified duration (in seconds) and reduces the bitrate to 64 kbps.
    """
    command = ['ffmpeg', '-ss', str(start_time), '-i', input_file, '-t', str(duration), '-acodec', 'libmp3lame', '-b:a', '64k', output_file]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return output_file
        else:
            return None
    except Exception as e:
        return None
