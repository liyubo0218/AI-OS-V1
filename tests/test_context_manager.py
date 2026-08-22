from core.context import ContextManager


def test_context():

    manager = ContextManager()


    result = manager.create(
        "user",
        "task"
    )


    assert result["user"] == "user"

    assert result["task"] == "task"


    print(
        "Context Manager PASS"
    )


if __name__ == "__main__":

    test_context()
