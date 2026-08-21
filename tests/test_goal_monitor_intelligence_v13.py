from goal_monitor.intelligence.goal_monitor_intelligence import GoalMonitorIntelligence


def test_goal_monitor_intelligence_v13():

    monitor = GoalMonitorIntelligence()

    result = monitor.monitor(
        "完成项目",
        "完成项目"
    )

    assert result["goal_status"] == "in_progress"

    assert result["deviation"] is False

    assert result["feedback"] == "goal_on_track"


    deviation_result = monitor.monitor(
        "完成项目",
        "偏离方向"
    )

    assert deviation_result["deviation"] is True

    assert deviation_result["feedback"] == "goal_deviation_detected"


    print(
        "Goal Monitor Intelligence V1.3 PASS"
    )


if __name__ == "__main__":
    test_goal_monitor_intelligence_v13()
