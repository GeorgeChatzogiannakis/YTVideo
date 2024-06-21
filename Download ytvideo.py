from wakepy import keep
import yt_dlp

def download_playlist(link):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'quiet' : True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract playlist info
            playlist_info = ydl.extract_info(link, download=False)
            total_videos = len(playlist_info['entries'])
            
            for index, video in enumerate(playlist_info['entries'], start=1):
                video_title = video.get('title', 'Unknown Title')
                print(f"\033[31mDownloading video {index}: {video_title} - {index}/{total_videos}\033[39m")
                ydl.download([video['webpage_url']])
            
            print("Download completed successfully.")
        except Exception as e:
            print(f"Error: {e}")
            return

def download_content(link):
    if "list=" in link.lower():
        playlist = input("The URL you entered belongs to a playlist. Would you like to download the entire playlist or just this video? (Press 'p' to download the playlist and 'v' to download the video): ")
        while playlist != 'p' and playlist != 'v':
            playlist = input("Invalid input. Please enter 'p' or 'v': ")
        if playlist == 'v':
            download_video(link)
        elif playlist == 'p':
            download_playlist(link)
    else:
        download_video(link)

def download_video(link):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True, 
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Processing video...")
            ydl.download([link])
            print("Download completed successfully.")
        except Exception as e:
            print(f"Error: {e}")
            return
        
def customList(videoList=None):
    if videoList is None:
        videoList = []
        link = input("Please paste the YouTube videos in the order you want to be downloaded (Enter 'ok' to finish):\n"+"Video 1: ")
        while link.lower() != 'ok' and link.lower() != 'end' and link.lower() != 'done':
            videoList.append(link)
            link = input(f"Video {len(videoList) + 1}: ")
    
    warning = input(f"You are about to download {len(videoList)} videos. Proceed? (y/n): ")
    while warning != 'y' and warning != 'n' and warning != '':
        smartass = input("Invalid Input! Please make sure you respond with the specified characters: ")
        if smartass == 'y' or smartass == 'n':
            warning = smartass
            break

    if warning.lower() == 'n':
        link = ""
        while link.lower() != "ok" and link.lower() != "end" and link.lower() != "done":
            link = input(f"Video {len(videoList) + 1}: ")
            if link.lower() != "ok" and link.lower != "end" and link.lower() != "done":
                videoList.append(link)
            else:
                warning = 'y'
    

    if warning.lower() == 'y'or warning.lower() == '':
        with keep.running():
            vid_or_aud = ""
            while vid_or_aud != "v" or vid_or_aud != "a":
                vid_or_aud = input("Please select output format. Type 'v' for video, 'a' for audio: ")
                if vid_or_aud == "v":
                    for index, video in enumerate(videoList,start=1):
                        print(f"\033[31m"+"Downloading video "+str(index)+"/"+str(len(videoList))+"\033[39m")
                        download_video(video)
                        print("Operation completed successfully.")
                    return
                if vid_or_aud == "a":
                    for index, video in enumerate(videoList,start=1):
                        print("Downloading audio "+str(index)+"/"+str(len(videoList)))
                        download_audio(video)
                        print("Operation completed successfully.")
                    return
    if warning.lower() == 'exit' or warning.lower() == 'e' or warning.lower() == 'x':
        print("Operation canceled.")

def download_channel_videos(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            channel_info = ydl.extract_info(channel_url, download=False)
            if 'entries' not in channel_info:
                print("No videos found")
                return []
            
            print("Collecting videos...")
            video_urls = [entry['url'] for entry in channel_info['entries']]
            customList(video_urls)
        except Exception as e:
            print(f"Error: {e}")
            return []

def download_audio(link=None):
    if link is None:
        link = input("Paste the URL of the YouTube audio you want to download: ")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Processing video...")
            info = ydl.extract_info(link, download=True)

            # Get the downloaded file name
            original_filename = info['title'] + '-' + info['id'] + '.mp3'

        print("Download completed successfully: ", original_filename)

    except Exception as e:
        print(f"Error: {e}")

def loadfile(textFile):
    mode = ""
    try:
        with open(textFile, 'r') as file:
            while mode != "a" or mode != "v":
                mode = input("Please choose output format (v: Video / a: Audio)> ")
                if mode == 'v':
                    for line in file:
                        download_video(line.strip())
                    return
                if mode == 'a':
                    for line in file:
                        download_audio(line.strip())
                    return
    except FileNotFoundError:
        print("File Not Found")

def main():   
    def validation(link):
            global valid
            valid = False
            if (not link.lower().startswith("https://www.youtube.") and not link.lower().startswith("https://youtu.be") and 
                not link.lower().startswith("https://m.youtube.") and link.lower() not in ["l", "m", "c", "txt", "q"]):
                print("Please Enter A YouTube URL")
            else:
                valid = True
    link = input("Enter the YouTube video or playlist URL to download.(Enter 'l' to batch download URLs, 'm' to download music (or press 'q' to quit): ")
    validation(link)
    if link.lower() == 'l':
        customList()
    elif link.lower() == 'm':
        download_audio()
    elif link.lower().find("@") != -1:
        download_channel_videos(link)
    elif link.lower() == 'c':
        print('Continuous mode initiated')
        while link.lower() != 'q':
            main()
    elif link.lower() == 'txt':
        textFile = input("Please input the file path with with the file containing the URLs you want to download:\n> ")
        loadfile(textFile)
    elif link.lower() == 'q': 
        print("Exiting script...")
        exit(0)
    else:
        if valid == True:
            download_content(link)


if __name__ == "__main__":
    main()
