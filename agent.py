from picoagents import Agent
from tools.current_time import get_current_time

from client.ollama_client import get_client


client = get_client()


dog_walk_agent = Agent(
    name="dog_walk_agent",
    description="An agent that helps decide whether it is a good time to walk the dog.",
    instructions="You are a helpful assistant that helps decide whether it is a good time to walk the dog.",
    model_client=client,
    tools=[get_current_time],
)