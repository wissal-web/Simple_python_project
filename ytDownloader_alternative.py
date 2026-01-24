import yt_dlp
import os
import subprocess
import sys

def check_ffmpeg():
    """Check if ffmpeg is installed"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    # Create downloads folder if it doesn't exist
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    # Check for ffmpeg
    ffmpeg_available = check_ffmpeg()
    
    # Configure yt-dlp options with better YouTube handling
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # Prefer mp4, fallback to best
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
        'socket_timeout': 30,
        'retries': 10,
        'fragment_retries': 10,
        'skip_unavailable_fragments': True,
        'external_downloader': 'aria2c' if False else None,  # Can add aria2c if available
        'extractor_args': {
            'youtube': {
                'skip': ['hls', 'dash'],  # Skip problematic formats
                'lang': ['en'],
            }
        }
    }
    
    # Add ffmpeg_location if available
    if ffmpeg_available:
        ydl_opts['ffmpeg_location'] = 'ffmpeg'
    
    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading video...")
        print("(This may take a few moments...)")
        info = ydl.extract_info(url, download=True)
        print(f"\n✅ Download complete: {info['title']}")
        
except yt_dlp.utils.DownloadError as e:
    print(f"❌ Download error: {str(e)}")
    print("\nTry using a different video or check if it's public/available in your region.")
except Exception as e:
    print(f"❌ An error occurred: {str(e)}")
    print("\nTip: Make sure the URL is correct and the video is publicly available.")
