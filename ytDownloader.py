from pytube import YouTube
import os

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    # Create YouTube object with headers to avoid blocking
    yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=False
    )
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    if yd:
        # Create downloads folder if it doesn't exist
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        
        print(f"Downloading: {yd.default_filename}")
        # Download the video to the downloads directory
        yd.download("downloads")
        
        print("Download complete.")
    else:
        print("No suitable stream found.")
except Exception as e:
    print("An error occurred:", str(e))
    print("\nNote: YouTube may have changed their API. Try using yt-dlp instead:")
    print("pip install yt-dlp")