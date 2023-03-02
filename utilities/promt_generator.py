def generate(data) -> str:
    prompts = [f"{key}: {value}" for value, key in data.items()]

    return ", ".join(prompts)