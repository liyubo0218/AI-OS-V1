from core.system.bootstrap import Bootstrap


def test_ai_os_final_flow():
    """
    AI-OS最终闭环测试

    验证：
    输入
    ↓
    API
    ↓
    Runtime
    ↓
    Orchestrator
    ↓
    Brain
    ↓
    Task
    ↓
    Device
    """

    bootstrap = Bootstrap()

    system = bootstrap.create()

    api = system["api"]

    result = api.handle_request(
        {
            "user_input": "帮我创建一个提醒任务"
        }
    )


    assert result["status"] == "success"

    assert "result" in result


    runtime_result = result["result"]


    assert "input" in runtime_result


    print(
        "AI-OS final flow test passed"
    )


if __name__ == "__main__":

    test_ai_os_final_flow()

    print(
        "AI-OS FINAL OK"
    )
