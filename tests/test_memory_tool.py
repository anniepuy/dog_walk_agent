import pytest

from memory_store import memory
from tools.memory import remember_fact

@pytest.mark.asyncio
async def test_remember_fact():
    result = await remember_fact("Dog prefers evening walks.")

    assert result == "Remembered: Dog prefers evening walks."
    assert memory.memories[-1].content == "Dog prefers evening walks."