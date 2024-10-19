
### SoundCloud Track Downloader & Song Identifier
This project downloads audio tracks from SoundCloud using yt-dlp, trims them to a specified duration using FFmpeg, and identifies the track using AudD.io's API. It serves as a simple way to extract and identify songs from SoundCloud, leveraging a combination of Python libraries and external tools.

**Features**
- Download Tracks from SoundCloud: Uses yt-dlp to extract audio from SoundCloud URLs and save them as MP3 files.
- Trim Audio Clips: Utilizes FFmpeg to trim the downloaded audio to a specified length, making it easier for Shazam to identify.
- Identify Songs with Audd.io API: Submits trimmed audio clips to Audd.io
- Retrieve Song Details: Extracts and displays details such as:
  - Song Title and Artist: The title of the identified song and the name of the artist.
  - Album Information: If available, the album name and cover art.
  - Lyrics: Fetches the lyrics of the identified track (if provided by Shazam).
  - Additional Data: Displays relevant metadata such as genre, release date, and popularity score.
