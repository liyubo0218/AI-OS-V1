from core.runtime.runtime import RuntimeCore
from core.runtime.state import RuntimeState


class MockRuntimeModule:

    def execute(
        self,
        task
    ):
        return {
            "status": "ok",
            "goal": task["goal"]
        }


def test_runtime_core():

    runtime = RuntimeCore()


    registered = runtime.register(
        "mock",
        MockRuntimeModule()
    )

    assert registered["status"] == "registered"
    assert runtime.registry.has(
        "mock"
    )


    result = runtime.run(
        "mock",
        {
            "goal": "准备会议"
        }
    )

    assert result["status"] == "completed"
    assert result["state"] == RuntimeState.COMPLETED
    assert result["result"]["goal"] == "准备会议"
    assert runtime.get_state() == RuntimeState.COMPLETED


    failed = runtime.run(
        "missing",
        {
            "goal": "未知任务"
        }
    )

    assert failed["status"] == "failed"
    assert failed["state"] == RuntimeState.FAILED


    print(
        "Runtime Core PASS"
    )


if __name__ == "__main__":
    test_runtime_core()
