from core.brain.memory_adapter import MemoryContextAdapter


def test_brain_memory_integration():

    adapter = MemoryContextAdapter()


    memory_context = adapter.get_memory_context(
        "AI-OS"
    )


    assert (
        "memory_context"
        in memory_context
    )


    assert (
        isinstance(
            memory_context["memory_context"],
            list
        )
    )


    # fallback validation

    empty_context = adapter.get_memory_context(
        None
    )


    assert (
        "memory_context"
        in empty_context
    )


    print(
        "Brain Memory Integration PASS"
    )


if __name__ == "__main__":
    test_brain_memory_integration()
