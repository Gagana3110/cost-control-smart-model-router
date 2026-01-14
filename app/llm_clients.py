import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def call_gpt4o(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content, 0.03  # mock cost

def call_llama(prompt: str):
    # Replace with actual local or hosted Llama call
    return f"[LLaMA Response] {prompt}", 0.005

def call_phi(prompt: str):
    # Replace with actual Phi-3 inference
    return f"[Phi-3 Response] {prompt}", 0.001
