# YTVideo
Ever wanted to download a YouTube video, but got fed up with all the malicious scripts that run in the background of the websites that offer to do the downloading for you?
Most of the online services that offer this kind of service, frequently make calls to some dodgy websites before they run, something I didn't appreciate very much when I found out.
I decided, therefore, to write a small python script that puts together some commonly wanted functionality someone would think of when downloading a video from YouTube, using ``yt_dlp``. 
This script does not necessarily need to be called from the Command Line Interface to run, unlike ``yt_dlp``, but it also does <b>NOT</b> contain all of the functionality found in ``yt_dlp``.

## <u>This script supports:</u><br>
<ul>
	  <li>  Downloading single YouTube videos</li>
	  <li>  Downloading audio from YouTube videos</li>
	  <li>  Downloading YouTube playlists</li>             
	  <li>  Downloading custom YouTube video queues</li>
	  <li>  Downloading a whole channel's content</li>
</ul>

## <u>How it works:</u><br>
This is a simple command line application, so unlike most of my other applications here, it doesn't have a Graphical User Interface (GUI).
A brief description of what each switch does is in the list below:<br><ul>
	<li>'`` ``' (Just the URL of a video) Downloads the video from YouTube in .mp4 format.</li>
 	<li>'``m``' will initiate music mode, which will create an audio file with the audio channel of the inserted video's URL.<br></li>
        <li> '``l``' (Lowercase 'L') initiates the 'custom list' mode, designed to accept multiple URLs, one by one. When one of the keywords "ok", "end",<br> or "done" is inputed, the list closes and the scripts asks if you want to download them as videos or audio-only. Once one of the two valid answers is given, it proceeds with the download of each URL in the desired format, in the order inserted in the script.<br></li>
	<li>'``c``' will initiate 'continuous mode', meaning it will enter a loop and constanlty prompt the user to input a URL of a video to process, after the previous operation is complete.<br></li>
	<li>'``txt``' will ask you to input the path to a txt file containing URLs you want to process, essentialy performing the same job with 'l', but taking its input from an existing text file, rather than line-by-line from the user.<br><b>NOTE: URLs in the file shuld be separated in different lines!</b><br></li>
	<li>'``q``' exits the current context. This will exit the script unless continious mode is active, in which case will exit continious mode, and will require a second 'q' input to terminate the script.</li>
