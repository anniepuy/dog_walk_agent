import asyncio

from agent import dog_walk_agent
from memory_store import add_memory


async def main():
    await add_memory("User lives in Atlanta, Georgia.")
    async for item in dog_walk_agent.run_stream(
        "What is the weather where I live right now?",
        verbose=True,
    ):
        print(item)


if __name__ == "__main__":
    asyncio.run(main())