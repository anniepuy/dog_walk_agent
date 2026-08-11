from picoagents import Agent
from tools.current_time import get_current_time
from tools.location import get_coordinates
from tools.weather import get_weather
from tools.memory import remember_fact
from tools.sunrise_sunset import get_sunrise_sunset
from tools.air_quality import get_air_quality
from memory_store import memory

from client.ollama_client import get_client

client = get_client()

dog_walk_agent = Agent(
    name="dog_walk_agent",
    description="An agent that helps decide whether it is a good time to walk the dog.",
    #instructions="You are a helpful assistant that helps decide whether it is a good time to walk the dog.",
    # Instructions after memory
    instructions=(
    "You are a helpful assistant that helps decide whether it is a good time "
    "to walk the dog. "
    "When the user tells you a stable fact about themselves or their dog "
    "that could be useful in future conversations, use the remember_fact tool "
    "to save it. "
    "Do not call weather, location, air quality or time tools unless they are needed "
    "to answer a question or complete a request."
    ),
    model_client=client,
    tools=[
        get_current_time,
        get_coordinates,
        get_weather,
        get_sunrise_sunset,
        get_air_quality,
        remember_fact
    ],
    memory=memory,
)
