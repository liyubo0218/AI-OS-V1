from core.goal_autonomy.goal_manager import GoalAutonomyManager


class MockPlanner:

    def create_plan(self, goal):
        return {
            "goal": goal,
            "status": "planned"
        }


class MockRuntime:

    def execute(self, plan):
        return {
            "status": "completed",
            "result": "会议准备完成"
        }



def test_goal_autonomy_integration_v2():

    goal_manager = GoalAutonomyManager()

    planner = MockPlanner()

    runtime = MockRuntime()


    goal = goal_manager.create_goal(
        "goal_001",
        "准备明天会议"
    )


    plan = planner.create_plan(
        goal["goal"]
    )


    result = runtime.execute(
        plan
    )


    assert result["status"] == "completed"


    state = goal_manager.update_progress(
        "goal_001",
        1
    )


    assert state["status"] == "completed"


    feedback = goal_manager.check_deviation(
        "goal_001"
    )


    assert feedback["deviation"] is False


    print(
        "Goal Autonomy Integration V2 PASS"
    )


if __name__ == "__main__":
    test_goal_autonomy_integration_v2()
