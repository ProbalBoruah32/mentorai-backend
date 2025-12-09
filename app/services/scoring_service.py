import re
from app.services.models.score_models import ScoreResponse


def evaluate_transcript(text: str) -> ScoreResponse:

    clarity = min(10, max(1, 10 - text.count("?")))
    pacing = min(10, 10 - text.count("..."))
    filler_words = len(re.findall(r"\b(um|uh|hmm|aaa)\b", text.lower()))
    fluency = max(1, 10 - filler_words)

    overall = round((clarity + pacing + fluency) / 3, 2)

    return ScoreResponse(
        clarity=clarity,
        pacing=pacing,
        fluency=fluency,
        overall=overall,
        transcript=text
    )
