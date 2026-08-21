from core.integration.system_integration import SystemIntegration


class MockBrain:

    def analyze(self, text):
        return {
            "goal": text,
            "intent": "general_task"
        }


class MockMemory:

    def analyze(self, text):
        return {
            "context_summary": text
        }


class MockPlanner:

    def create_plan(self, brain, memory):
        return {
            "task": brain["goal"],
            "required_capability": "task_execution"
        }


class MockAgentManager:

    def select_agent(self, capability):
        return {
            "selected_agents": [
                "task_agent"
            ]
        }

    def coordinate_agents(self, agents, task):
        return {
            "execution_plan": agents,
            "result": task
        }


class MockGoalMonitor:

    def monitor(self, goal, result):
        return {
            "deviation": False,
            "feedback": "goal_on_track"
        }


def test_system_integration_v13():

    system = SystemIntegration(
        MockBrain(),
        MockMemory(),
        MockPlanner(),
        MockAgentManager(),
        MockGoalMonitor()
    )

    result = system.process(
        "准备会议"
    )

    assert result["brain"]["goal"] == "准备会议"

    assert result["execution"]["result"] == "准备会议"

    assert result["feedback"]["deviation"] is False

    print(
        "System Integration V1.3 PASS"
    )


if __name__ == "__main__":
    test_system_integration_v13()
