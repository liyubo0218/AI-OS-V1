from core.memory.classifier import MemoryClassifier


def test_memory_classifier():

    classifier = MemoryClassifier()


    user = classifier.classify(
        "我喜欢自动化工作流"
    )

    assert user["type"] == "user"


    task = classifier.classify(
        "完成AI-OS任务"
    )

    assert task["type"] == "task"


    goal = classifier.classify(
        "长期目标进度"
    )

    assert goal["type"] == "goal"


    context = classifier.classify(
        "当前会话信息"
    )

    assert context["type"] == "context"


    print(
        "Memory Classifier PASS"
    )


if __name__ == "__main__":
    test_memory_classifier()
