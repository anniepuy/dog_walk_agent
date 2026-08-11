from picoagents import OpenAIChatCompletionClient

OLLAMA_BASE_URL = "http://localhost:11434/v1"
DEFAULT_MODEL = "qwen3:30b"

def get_client(model: str = DEFAULT_MODEL) -> OpenAIChatCompletionClient:
    """Return a PicoAgent client connected to local Ollama."""
    return OpenAIChatCompletionClient(
        model=model,
        base_url=OLLAMA_BASE_URL,
        api_key="ollama",
    )