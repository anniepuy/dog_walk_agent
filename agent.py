from picoagents import Agent
from clients.ollama_client import get_client

dog_walk_agent = Agent(
    name="dog_walk_agent",
    instructions="You are a helpful assistant that helps decide whether it is a good time to walk the dog.",
    model_client=get_client(),
)