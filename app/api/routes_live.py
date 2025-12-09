from fastapi import APIRouter, UploadFile, File

from app.utils.file_utils import save_upload_file, extract_audio
from app.services.whisper_service import transcribe_audio
from app.services.scoring_service import evaluate_transcript
from app.services.gpt_fallback import tiny_gpt_fallback

router = APIRouter()

@router.post("/live")
async def live_upload(file: UploadFile = File(...)):
    # save temp file
    temp_path = save_upload_file(file)

    # convert video -> audio
    if temp_path.endswith(".mp4"):
        audio_path = extract_audio(temp_path)
    else:
        audio_path = temp_path

    # run whisper
    transcript = transcribe_audio(audio_path)

    # if whisper fails => use tiny GPT fallback
    if transcript is None or transcript.strip() == "":
        print("⚠ Whisper failed → using GPT fallback")

        fallback = tiny_gpt_fallback()

        return {
            "transcript": fallback["summary"],
            "score": {"overall": fallback["score"], "source": "gpt-fallback"}
        }

    # normal whisper scoring
    score = evaluate_transcript(transcript)

    return {
        "transcript": transcript,
        "score": score
    }
