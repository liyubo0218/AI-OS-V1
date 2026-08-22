from core.goal_v2 import ActiveGoalMonitor


def test_goal_v2():


    monitor = ActiveGoalMonitor()


    monitor.create_goal(
        "001",
        "完成报告"
    )


    result = monitor.monitor_goal(
        "001"
    )


    assert result["deviation"]["deviation"] is True


    monitor.tracker.update_progress(
        "001",
        50
    )


    result = monitor.monitor_goal(
        "001"
    )


    assert result["deviation"]["deviation"] is False


    print(
        "Active Goal Monitor PASS"
    )


if __name__ == "__main__":

    test_goal_v2()
