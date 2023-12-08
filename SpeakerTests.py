import os


def play_audio_file_windows(file_path):
    try:
        # Use start to open the default media player for the MP3 file (Windows command)
        os.system(f"start {file_path}")
    except Exception as e:
        print(f"Error playing audio: {e}")

if __name__ == "__main__":
    audio_file_path = r"C:\\Users\\masca\\Downloads\\Jarvis.mp3"  # Replace with the path to your MP3 audio file
    play_audio_file_windows(audio_file_path)
