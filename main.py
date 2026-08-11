import asyncio

from agent import dog_walk_agent
from memory_store import add_memory


#async def main():
 #   await add_memory("User lives in Atlanta, Georgia.")
 #   async for item in dog_walk_agent.run_stream(
 #       "What is the weather where I live right now?",
 #       verbose=True,
 #   ):
  #    print(item)

# post add memory recall
async def main():
    response = await dog_walk_agent.run(
        "I live in Atlanta, Georgia. Should I walk the dog right now?"
    )

    final_message = response.messages[-1]

    print(final_message.structured_content)

if __name__ == "__main__":
    asyncio.run(main())