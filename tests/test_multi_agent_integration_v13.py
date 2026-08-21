from agent_manager.intelligence.multi_agent_manager import MultiAgentManager


class MockPlanner:

    def create_plan(self, task):
        return {
            "task": task,
            "required_capability": "task_execution"
        }


def test_multi_agent_integration_v13():

    planner = MockPlanner()

    manager = MultiAgentManager()

    manager.register_agent(
        "task_agent",
        "task_execution"
    )

    plan = planner.create_plan(
        "执行测试任务"
    )

    selected = manager.select_agent(
        plan["required_capability"]
    )

    result = manager.coordinate_agents(
        selected["selected_agents"],
        plan["task"]
    )

    assert "task_agent" in selected["selected_agents"]

    assert result["result"] == "执行测试任务"

    print(
        "Multi-Agent Integration V1.3 PASS"
    )


if __name__ == "__main__":
    test_multi_agent_integration_v13()
