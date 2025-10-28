import os
import requests

# Load Perplexity API Key from environment variable (set via GitHub Secrets!)
api_key = "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"

with open("pr.diff", "r") as f:
    diff = f.read()

prompt = f"""
Given this Python PR diff, generate suggested unit tests and doc explanations:
{diff[:3000]}
"""

response = requests.post(
    "https://api.perplexity.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "llama-3-sonar-large-32k-online",  # Optionally change model name if needed
        "messages": [{
            "role": "user",
            "content": prompt
        }],
        "max_tokens": 800
    },
    timeout=60
)

result = response.json()
ai_text = result.get("choices", [{}])[0].get("message", {}).get("content", "No result!")

with open("suggestions.txt", "w") as sf:
    sf.write(ai_text)
