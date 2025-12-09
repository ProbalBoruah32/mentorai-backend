import openai

openai.api_key = "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"

def tiny_gpt_fallback():
    """
    Returns a small stamped message + approximate score.
    Uses very few tokens.
    """

    prompt = """
You are assisting an educational scoring system.
Whisper failed to fully transcribe audio.

Give a VERY SHORT FAKE summary (1-2 lines)
and a SIMPLE score between 1–5.

Format:
summary: <your summary>
score: <number>
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",   # cheapest model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=40
        )

        text = response.choices[0].message["content"]

        # Parse output
        result = {"summary": "", "score": 0}

        for line in text.split("\n"):
            if "summary:" in line.lower():
                result["summary"] = line.split(":",1)[1].strip()
            if "score:" in line.lower():
                result["score"] = line.split(":",1)[1].strip()

        return result

    except Exception as e:
        print("GPT fallback error:", e)
        return {"summary": "Error generating summary", "score": 0}
