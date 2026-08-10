import pytest

from memory_store import memory, add_memory

@pytest.mark.asyncio
async def test_add_memory():
    await add_memory("User lives in Atlanta, Georgia")

    assert len(memory.memories) == 1

    print(memory.memories)