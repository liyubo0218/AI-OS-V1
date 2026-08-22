from core.runtime.task_runtime import TaskRuntime


def test_task_runtime_v13():

    runtime = TaskRuntime()

    task = runtime.create_task(
        "准备明天会议"
    )

    assert task["goal"] == "准备明天会议"
    assert task["status"] == "created"


    result = runtime.update_status(
        "task_001",
        "completed",
        "会议准备完成"
    )


    assert result["status"] == "completed"
    assert result["result"] == "会议准备完成"


    print(
        "Task Runtime V1.3 PASS"
    )


if __name__ == "__main__":
    test_task_runtime_v13()
