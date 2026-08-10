from picoagents.memory import ListMemory, MemoryContent

memory = ListMemory(max_memories=50)

async def add_memory(content: str)-> None:
    """Add a text memory to the agent's memory store."""
    await memory.add(
        MemoryContent(
            content=content,
            mime_type="text/plain",
        )
    )