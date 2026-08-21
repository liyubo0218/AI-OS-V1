from core.memory.interface import MemoryInterface


def test_memory_interface():

    memory = MemoryInterface()


    saved = memory.save(
        "memory_interface_test",
        "task",
        "Memory Interface Regression"
    )


    assert (
        saved["content"]
        ==
        "Memory Interface Regression"
    )


    memories = memory.retrieve()

    assert (
        len(memories)
        >
        0
    )


    result = memory.search(
        "Regression"
    )

    assert (
        len(result)
        >
        0
    )


    context = memory.build_context(
        "Regression"
    )


    assert (
        "memories"
        in
        context
    )


    print(
        "Memory Interface PASS"
    )


if __name__ == "__main__":

    test_memory_interface()
