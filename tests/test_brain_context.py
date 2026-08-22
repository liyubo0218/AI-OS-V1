from core.brain.context.brain_adapter import BrainAdapter


def test_brain_context():


    brain = BrainAdapter()


    result = brain.understand(
        "提醒我明天开会"
    )


    assert result["intent"] == "reminder"

    assert result["goal"] == "reminder_task"

    assert result["context"]["time"] == "tomorrow"


    print(
        "AI Brain Enhancement PASS"
    )


if __name__ == "__main__":

    test_brain_context()
