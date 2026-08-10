import asyncio

from agent import dog_walk_agent


async def main():
    async for item in dog_walk_agent.run_stream(
        "Hello! What is your job?",
        verbose=True,
    ):
        print(item)


if __name__ == "__main__":
    asyncio.run(main())