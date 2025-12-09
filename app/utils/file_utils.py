import tempfile
import ffmpeg
import os

def save_upload_file(upload_file):
    """Save incoming file to a temp path"""
    suffix = upload_file.filename
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(upload_file.file.read())
    temp_file.close()
    return temp_file.name


def extract_audio(video_path: str) -> str:
    """Convert MP4 → WAV for Whisper"""
    audio_path = video_path + ".wav"
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar=16000)
        .overwrite_output()
        .run(quiet=True)
    )
    return audio_path
