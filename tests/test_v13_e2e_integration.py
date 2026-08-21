from core.brain.intelligence.brain_intelligence import BrainIntelligence
from core.memory.intelligence.memory_intelligence import MemoryIntelligence
from agent_manager.intelligence.multi_agent_manager import MultiAgentManager
from goal_monitor.intelligence.goal_monitor_intelligence import GoalMonitorIntelligence


class MockPlanner:

    def create_plan(
        self,
        brain_result,
        memory_result
    ):
        return {
            "task": brain_result["goal"],
            "required_capability": "task_execution"
        }


def test_v13_e2e_integration():

    brain = BrainIntelligence()

    memory = MemoryIntelligence()

    planner = MockPlanner()

    agent_manager = MultiAgentManager()

    goal_monitor = GoalMonitorIntelligence()


    agent_manager.register_agent(
        "task_agent",
        "task_execution"
    )


    brain_result = brain.analyze(
        "帮我准备明天会议"
    )


    memory_result = memory.analyze(
        "用户习惯提前准备会议"
    )


    plan = planner.create_plan(
        brain_result,
        memory_result
    )


    agents = agent_manager.select_agent(
        plan["required_capability"]
    )


    execution = agent_manager.coordinate_agents(
        agents["selected_agents"],
        plan["task"]
    )


    feedback = goal_monitor.monitor(
        brain_result["goal"],
        execution["result"]
    )


    assert brain_result["goal"] == "帮我准备明天会议"

    assert memory_result["importance_score"] == 1

    assert "task_agent" in agents["selected_agents"]

    assert execution["result"] == "帮我准备明天会议"

    assert feedback["deviation"] is False


    print(
        "AI-OS V1.3 E2E Integration PASS"
    )


if __name__ == "__main__":
    test_v13_e2e_integration()
