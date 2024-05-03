# YTVideo
Ever wanted to download a YouTube video, but got fed up with all the phishing scripts that run in the background of the websites that offer to do the downloading for you?
Most of the online services that offer this kind of service, frequently hide some nasty code within them, so I decided to write a small python script using the ``yt_dlp`` and ``pytube`` libraries to accommodate just that. (Even thought there might be hundereds out there, if not more)

## <u>This script supports:</u><br>
<ul>
	  <li>  Downloading single YouTube videos</li>
	  <li>  Downloading audio from YouTube videos</li>
	  <li>  Downloading YouTube playlists</li>             
	  <li>  Downloading custom YouTube video queues</li>
</ul>

## <u>How it works:</u><br>
This is a simple command line application, so unlike most of my other applications here, it doesn't have a Graphical User Interface (GUI). 
The most basic functionallity (and how to utilize it within the script) is explained within the script, there are some features, however, 
that, in order not to fill an entire window with text, I didn't mention within the script. 
You can find what every whitch does in the list below if you are too bored to read the script:<br><ul>
	<li> '``l``' (Lowercase 'L') initiates the 'custom list' mode, designed to accept multiple URLs, one by one. When one of the keywords "ok", "end",<br> or "done" is inputed, the list closes and the scripts asks if you want to download them as videos or audio-only. Once one of the two valid answers is given, it proceeds with the download of each URL in the desired format, in the order inserted in the script.<br></li>
	<li>'``m``' will initiate music mode, and it will create an audio file containing the audio channel of the video's URL you inserted.<br></li>
	<li>'``c``' will initiate 'continuous mode', meaning it will enter a loop and constanlty prompt the user to input a URL of a video to process, after the previous operation is complete.<br></li>
	<li>'``txt``' will ask you to input the path to a txt file containing URLs you want to process, essentialy performing the same job with 'l', but taking its input from an existing text file, rather than line-by-line from the user.<br></li>
	<li>'``q``' exits the script. Unless continious mode is active, in which case will exit continious mode, and will require a second 'q' input to terminate the script.</li>
