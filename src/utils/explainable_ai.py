import subprocess

def generate_local_ollama_explanation(prompt: str) -> str:
    """
    Run local Ollama model (e.g., ollama/gpt-small) via CLI with the given prompt.
    Returns generated explanation text. Assumes Ollama CLI and model installed.
    """
    try:
        completed = subprocess.run(
            ["ollama", "run", "ollama/gpt-small"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return completed.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as err:
        return f"⚠️ Ollama call error: {err.stderr.decode('utf-8')}"

def build_ollama_prompt(label: str, confidence: float, message: str, keywords: list[str]) -> str:
    """
    Construct a clear prompt explaining phishing detection results for Ollama.
    """
    keys = ", ".join(keywords)
    return f"""
You are a cybersecurity assistant. The phishing model predicted: {label} with confidence {confidence:.2f}.
Key indicators include: {keys}.

Explain in clear and concise terms why this message may be phishing or safe,
with advice for a non-technical user.

Message:
{message}
""".strip()

def explain_with_ollama(label, confidence, message, keywords):
    prompt = build_ollama_prompt(label, confidence, message, keywords)
    explanation = generate_local_ollama_explanation(prompt)
    return explanation
