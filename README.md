# 🐕 Dog Walk Agent

A local-first AI agent that decides whether it's a good time to walk the dog — by
reasoning over live weather, air quality, and daylight, and returning a _structured_
recommendation.

Ask it **"Should I walk the dog right now?"** and it resolves your location, pulls
current conditions, and replies with one of `WALK`, `SHORT_WALK`, `WAIT`, or `SKIP`
— plus the reasons and risks behind the call.

## How it works

A tool-calling agent built on [`picoagents`](https://pypi.org/project/picoagents/),
running against a **local LLM via [Ollama](https://ollama.com/)** (default `qwen3:30b`).
The model decides which tools to call, then returns a typed `WalkDecision` instead of
free-form text.

| Tool                 | What it does                            |
| -------------------- | --------------------------------------- |
| `get_current_time`   | Current local time                      |
| `get_coordinates`    | Geocodes a place name → lat/long        |
| `get_weather`        | Live weather (Open-Meteo)               |
| `get_air_quality`    | Live US AQI / PM2.5 / PM10 (Open-Meteo) |
| `get_sunrise_sunset` | Daylight window                         |
| `remember_fact`      | Saves a stable fact to agent memory     |

**Structured output** (`models/walk_decision.py`):

```python
class WalkDecision(BaseModel):
    recommendation: Literal["WALK", "SHORT_WALK", "WAIT", "SKIP"]
    duration_minutes: Optional[int]
    reasons: List[str]
    risks: List[str]
```

## Set up

ollama pull qwen3:30b # install Ollama first, then pull the model
pip install -r requirements.txt

## Use

python main.py

## Tests

pytest

## Project structure

agent.py # Agent: tools, memory, structured output
main.py # Entry point / demo query
client/ollama_client.py # Local Ollama (OpenAI-compatible) client
models/walk_decision.py # WalkDecision output schema
memory_store.py # Agent memory (ListMemory)
tools/ # time, location, weather, air_quality, sunrise_sunset, memory
tests/ # pytest suite per tool

## Notes & Roadmap

Memory is an in-process ListMemory, so remembered facts don't persist across runs yet — persisting to disk is the natural next step.
The entry point hardcodes a sample prompt; a small CLI / interactive loop would make it usable day-to-day.
