from core.brain.memory_adapter import MemoryContextAdapter


def test_memory_context_adapter():

    adapter = MemoryContextAdapter()


    result = adapter.get_memory_context(
        "AI-OS"
    )


    assert (
        "memory_context"
        in result
    )


    assert (
        isinstance(
            result["memory_context"],
            list
        )
    )


    empty = adapter.get_memory_context(
        None
    )


    assert (
        "memory_context"
        in empty
    )


    print(
        "Memory Context Adapter PASS"
    )


if __name__ == "__main__":
    test_memory_context_adapter()
