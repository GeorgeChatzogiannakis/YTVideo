from pytube import Playlist, exceptions
from wakepy import keep
import yt_dlp

def download_playlist(link):
    with keep.running():
        try:
            youtube_playlist = Playlist(link)
            total_Videos = len(youtube_playlist.video_urls)
            if total_Videos < 1 :
                print("No videos found")
                return
            print("{} videos found in playlist.".format(total_Videos))
            for index, video_url in enumerate(youtube_playlist.video_urls,start=1):
                print(f"Downloading video " + str(index)+"/"+str(total_Videos))
                download_video(video_url)
            print("Download of playlist completed successfully.")
        except Exception as e:
            print(f"Error: {e}")
            if isinstance(e, exceptions.AgeRestrictedError):
                download_video()

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
#region
# def google_authenticate(link):
    # SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    # creds = None
    # if os.path.exists('token.pickle'):
    #     print("Loading Credentials...")
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         print("Refreshing Token...")
    #         creds.refresh(Request())
    #     else:
    #         print("Fetching New Token...")
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=8080)
    #     with open('token.pickle', 'wb') as token:
    #         print("Saving Credentials to file...")
    #         pickle.dump(creds, token)
    # return download_ar_video(link)
#endregion
def customList():
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
                        print(f"Downloading video "+str(index)+"/"+str(len(videoList)))
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
    elif link.lower() == 'c':
        print('Continuous mode initiated')
        while link.lower() != 'q':
            main()
    elif link.lower() == 'txt':
        textFile = input("Please input the file path with with the file containing the URLs you want to download:\n> ")
        loadfile(textFile)
    elif link.lower() == 'q': 
        print("Exiting the script...")
        exit(0)
    else:
        if valid == True:
            download_content(link)


if __name__ == "__main__":
    main()