from core.goal import GoalMonitor


def test_goal_monitor():


    monitor = GoalMonitor()


    monitor.create_goal(
        "001",
        "完成测试任务"
    )


    monitor.update_goal(
        "001",
        "completed"
    )


    result = monitor.get_goal(
        "001"
    )


    assert result["status"] == "completed"


    print(
        "Goal Monitor PASS"
    )


if __name__ == "__main__":

    test_goal_monitor()
