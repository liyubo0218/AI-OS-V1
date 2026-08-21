from agent_manager.intelligence.multi_agent_manager import MultiAgentManager


def test_multi_agent_manager_v13():

    manager = MultiAgentManager()

    register_result = manager.register_agent(
        "task_agent",
        "task_execution"
    )

    assert register_result["registered"] is True

    selected = manager.select_agent(
        "task_execution"
    )

    assert "task_agent" in selected["selected_agents"]

    execution = manager.coordinate_agents(
        ["task_agent"],
        "完成任务"
    )

    assert execution["execution_plan"] == [
        "task_agent"
    ]

    assert execution["result"] == "完成任务"

    print(
        "Multi-Agent Collaboration V1.3 PASS"
    )


if __name__ == "__main__":
    test_multi_agent_manager_v13()
