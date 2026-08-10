import asyncio

from agent import dog_walk_agent


async def main():
    async for item in dog_walk_agent.run_stream(
        "What is the weather in Atlanta, Georgia right now?",
        verbose=True,
    ):
        print(item)


if __name__ == "__main__":
    asyncio.run(main())