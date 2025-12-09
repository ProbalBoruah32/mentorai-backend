from fastapi import APIRouter, UploadFile, File
from app.utils.file_utils import save_upload_file, extract_audio
from app.services.whisper_service import transcribe_audio
from app.services.scoring_service import evaluate_transcript

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        temp_path = save_upload_file(file)

        # Convert video → audio if needed
        if temp_path.lower().endswith(".mp4") or temp_path.lower().endswith(".mkv"):
            audio_path = extract_audio(temp_path)
        else:
            audio_path = temp_path

        # Transcribe using Whisper
        transcript = transcribe_audio(audio_path)

        if not transcript or transcript == "Transcription failed":
            return {"error": "Unable to transcribe audio", "transcript": transcript}

        # Score transcript (ensure dict output)
        score = evaluate_transcript(transcript)

        if hasattr(score, "dict"):  # if Pydantic model
            score = score.dict()

        return {
            "transcript": transcript,
            "score": score
        }

    except Exception as e:
        print("UPLOAD API ERROR:", e)
        return {"error": "Upload processing failed", "details": str(e)}
