from transformers import pipeline
import torch

ASR_MODEL = "prob12/mentorai_english_hindi"

print("⏳ Loading Whisper ASR model...")

device = 0 if torch.cuda.is_available() else -1

asr_pipeline = pipeline(
    "automatic-speech-recognition",
    model=ASR_MODEL,
    chunk_length_s=20,
    device=device
)

print("✅ Whisper model loaded successfully!")


def transcribe_audio(path: str):
    try:
        result = asr_pipeline(
            path,
            chunk_length_s=20,
            return_timestamps=False  # 🔥 FIX: prevents slice error
        )
        return result["text"]

    except Exception as e:
        print("🚨 Transcription Error:", e)
        return "Transcription failed"
