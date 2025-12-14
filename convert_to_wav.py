# Responsible for converting any file to .wav format

from pathlib import Path # modern - more stable - way to work with files and folders
import subprocess # allows me to run programs as if they are in the terminal

# import os # import the python operating system to access directories
# def convert_video_to_mp3(input_file, output_file):
#     ffmpeg_cmd = [
#         "ffmpeg",
#         "-i", input_file,           # Input File Path
#         "-vn",                      # -vn = disable video
#         "-acodec", "libmp3lame",    # Choose the MP3 encoder
#         "-ab", "192k",              # Audio bitrate 192kbps
#         "-ar", "44100",             # Audio sample rate 44.1 kHz
#         "-y",                       # overwrite output
#         output_file                 # Output File Path  
#     ]

#     try:
#         subprocess.run(ffmpeg_cmd, check = True)
#         print ("Success")
#     except subprocess.CalledProcessError as e:
#         print ("Conversion failed!")

def convert_to_wav(input_file):
    """
    Converts ANY audio/video file to: 
    - WAV
    - 44.1 kHz
    - 16-bit PCM
    - stero


    Saves output to bassgen/data/wav/
    
    """

    # Turns a string into a a path object
    input_path = Path(input_file)

    # Define output directory
    """
    * __file__ --> current script location
    * .resolve() --> Converts it to an absolute path
        - removes ambiguity like ../
    *  .parents --> list of all parent directories
        - .parents[0] --> audio_processing/
        - .parents[1] --> src/
        - .parents[2] --> BassGen/
    * output_dir.mkdir(parents = True, exist_ok = True)
        - Create directory if it doesn't exist
        - Don't crash if it already exists
        - Create missing parent folders automatically
    
    """
    project_root = Path(__file__).resolve().parents[2]  
    output_dir = project_root / "data" / "wav"
    output_dir.mkdir(parents = True, exist_ok = True)

    # Output File Path
    output_file = output_dir / f"{input_path.stem}.wav" # .stem removes whatever stem is attached to the file (.wav, .mp3, .mp4, etc)

    ffmpeg_cmd = [
        "ffmpeg",               # call ffmpeg
        "-i", str(input_path),  # input path as a string
        "-vn",                  # Remove video - only want audio
        "-ac", "2",             # Stereo audio (1 would be mono)
        "-ar", "44100",         # Sample Rate
        "-sample_fmt", "s16",   # 16-bit PCM
        "-y",                   # overwrite if exists
        str(output_file)
    ]

    try:
        subprocess.run(ffmpeg_cmd, check = True)
        print ("Success")
        return output_file
    except subprocess.CalledProcessError as e:
        print ("Conversion failed!")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]  
    input_dir = project_root / "data" / "input" / "ryanGot.mp4"
    # test_input = "data/input/ryanGot.mp4"
    output = convert_to_wav(input_dir)
    print(f"Converted to: {output}")