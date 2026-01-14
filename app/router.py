def classify_prompt(prompt: str) -> str:
    prompt_lower = prompt.lower()

    if any(word in prompt_lower for word in ["summarize", "translate", "define"]):
        return "simple"

    if any(word in prompt_lower for word in ["explain", "compare", "analyze"]):
        return "medium"

    if any(word in prompt_lower for word in ["code", "algorithm", "optimize", "system design"]):
        return "hard"

    return "medium"
