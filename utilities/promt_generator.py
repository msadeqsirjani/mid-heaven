def generate(data) -> str:
    prompts = [f"{value}" for key, value in data.items()]

    return ",".join(prompts)
