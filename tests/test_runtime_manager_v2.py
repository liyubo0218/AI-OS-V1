from core.runtime.runtime_manager import RuntimeManager


def test_runtime_manager_v2():

    runtime = RuntimeManager()


    created = runtime.create_task(
        "task_001",
        "iphone_agent",
        "准备会议"
    )

    assert created["status"] == "created"


    state = runtime.update_state(
        "task_001",
        "executing"
    )

    assert state["current_state"] == "executing"


    runtime.update_context(
        "task_001",
        {
            "agent": "iphone_agent",
            "capability": "calendar"
        }
    )


    result = runtime.record_result(
        "task_001",
        "会议创建完成"
    )

    assert result["status"] == "recorded"


    task = runtime.get_task(
        "task_001"
    )

    assert task["state"] == "executing"
    assert task["result"] == "会议创建完成"


    print(
        "Runtime Manager V2 PASS"
    )


if __name__ == "__main__":
    test_runtime_manager_v2()
