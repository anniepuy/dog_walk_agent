from memory_store import add_memory

async def remember_fact(fact: str) -> str:
    """Remember a useful fact about the user or dog for future conversations."""
    await add_memory(fact)

    return f"Remembered: {fact}"