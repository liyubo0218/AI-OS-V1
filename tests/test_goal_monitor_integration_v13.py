from goal_monitor.intelligence.goal_monitor_intelligence import GoalMonitorIntelligence


class MockPlanner:

    def receive_feedback(self, feedback):
        return {
            "planner_updated": True,
            "feedback": feedback
        }


def test_goal_monitor_integration_v13():

    monitor = GoalMonitorIntelligence()

    planner = MockPlanner()

    result = monitor.monitor(
        "完成AI-OS开发",
        "完成AI-OS开发"
    )

    planner_result = planner.receive_feedback(
        result["feedback"]
    )

    assert result["deviation"] is False

    assert result["feedback"] == "goal_on_track"

    assert planner_result["planner_updated"] is True

    print(
        "Goal Monitor Integration V1.3 PASS"
    )


if __name__ == "__main__":
    test_goal_monitor_integration_v13()
