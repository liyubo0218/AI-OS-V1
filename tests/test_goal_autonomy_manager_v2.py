from core.goal_autonomy.goal_manager import GoalAutonomyManager


def test_goal_autonomy_manager_v2():

    manager = GoalAutonomyManager()


    goal = manager.create_goal(
        "goal_001",
        "准备明天会议"
    )


    assert goal["goal"] == "准备明天会议"
    assert goal["status"] == "created"


    state = manager.update_progress(
        "goal_001",
        0.5
    )


    assert state["status"] == "in_progress"


    feedback = manager.check_deviation(
        "goal_001"
    )


    assert feedback["deviation"] is False


    print(
        "Goal Autonomy Manager V2 PASS"
    )


if __name__ == "__main__":
    test_goal_autonomy_manager_v2()
