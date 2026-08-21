from core.brain.intelligence.brain_intelligence import BrainIntelligence


class MockPlanner:

    def receive_goal(self, brain_result):
        return {
            "planner_received": True,
            "goal": brain_result["goal"]
        }


def test_brain_intelligence_integration_v13():

    brain = BrainIntelligence()

    planner = MockPlanner()

    result = brain.analyze(
        "安排明天会议"
    )

    planner_result = planner.receive_goal(
        result
    )

    assert result["intent"] == "general_task"

    assert planner_result["planner_received"] is True

    assert planner_result["goal"] == "安排明天会议"

    assert "recommendation" in result

    print(
        "Brain Intelligence Integration V1.3 PASS"
    )


if __name__ == "__main__":
    test_brain_intelligence_integration_v13()
