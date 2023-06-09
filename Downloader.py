import argparse
from pytube import YouTube

class Downloader:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-v", dest="video", help="Download video")
        self.parser.add_argument("-a", dest="audio", help="Download audio")
        self.args = self.parser.parse_args()

    def download_video(self, link):
        try:
            youtube = YouTube(link)
            video = youtube.streams.get_highest_resolution()
            video.download()
            print("Video downloaded successfully.")

        except Exception as e:
            print(f"An error occurred while downloading the video: {str(e)}")

    def download_audio(self, link):
        try:
            youtube = YouTube(link)
            audio = youtube.streams.get_audio_only()
            audio.download()
            print("Audio downloaded successfully.")

        except Exception as e:
            print(f"An error occurred while downloading the audio: {str(e)}")

    def run(self):
        if self.args.video:
            self.download_video(self.args.video)

        elif self.args.audio:
            self.download_audio(self.args.audio)
        
        else:
            print("No option selected. Please use either -v or -a.")

if __name__ == "__main__":
    downloader = Downloader()
    downloader.run()
