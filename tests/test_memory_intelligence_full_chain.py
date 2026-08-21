from core.memory.classifier import MemoryClassifier
from core.memory.interface import MemoryInterface
from core.memory.context_builder import ContextBuilder


def test_memory_intelligence_full_chain():

    classifier = MemoryClassifier()

    memory = MemoryInterface()

    builder = ContextBuilder(
        memory
    )


    content = (
        "用户喜欢自动化工作流"
    )


    classified = classifier.classify(
        content
    )


    assert (
        classified["type"]
        ==
        "user"
    )


    saved = memory.save(
        "memory_full_chain_001",
        classified["type"],
        content
    )


    assert (
        saved["type"]
        ==
        "user"
    )


    result = memory.search(
        "自动化"
    )


    assert (
        len(result)
        >
        0
    )


    context = builder.build_context(
        "自动化"
    )


    assert (
        "context"
        in context
    )


    assert (
        len(context["context"])
        >
        0
    )


    print(
        "Memory Intelligence Full Chain PASS"
    )


if __name__ == "__main__":
    test_memory_intelligence_full_chain()
