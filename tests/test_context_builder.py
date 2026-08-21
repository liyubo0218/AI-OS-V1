from core.memory.context_builder import ContextBuilder
from core.memory.interface import MemoryInterface


def test_context_builder():

    memory = MemoryInterface()


    memory.save(
        "context_builder_test_001",
        "task",
        "AI-OS Context Builder Regression"
    )


    builder = ContextBuilder(
        memory
    )


    result = builder.build_context(
        "Regression"
    )


    assert (
        "context"
        in result
    )


    assert (
        len(result["context"])
        >
        0
    )


    empty = builder.build_context()

    assert (
        "context"
        in empty
    )


    print(
        "Context Builder PASS"
    )


if __name__ == "__main__":
    test_context_builder()
