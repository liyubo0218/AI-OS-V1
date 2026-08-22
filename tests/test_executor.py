from core.executor import Executor


def test_executor():


    executor = Executor()


    executor.register_action(
        "hello",
        lambda x: {
            "result": "ok"
        }
    )


    result = executor.execute(
        "hello"
    )


    assert result["result"] == "ok"


    print(
        "Executor PASS"
    )


if __name__ == "__main__":

    test_executor()
