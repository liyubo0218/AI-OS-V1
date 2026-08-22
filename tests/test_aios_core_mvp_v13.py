from core.brain.intelligence.brain_intelligence import BrainIntelligence
from core.memory.intelligence.memory_intelligence import MemoryIntelligence
from core.planner.planner_engine import PlannerEngine
from core.runtime.task_runtime import TaskRuntime
from agents.assistant.personal_assistant_agent import PersonalAssistantAgent
from goal_monitor.intelligence.goal_monitor_intelligence import GoalMonitorIntelligence


def test_aios_core_mvp_v13():

    brain = BrainIntelligence()
    memory = MemoryIntelligence()
    planner = PlannerEngine()
    runtime = TaskRuntime()
    agent = PersonalAssistantAgent()
    monitor = GoalMonitorIntelligence()


    user_goal = "帮我准备明天会议"


    brain_result = brain.analyze(
        user_goal
    )

    memory_result = memory.analyze(
        user_goal
    )

    plan = planner.create_plan(
        brain_result["goal"],
        memory_result
    )

    task = runtime.create_task(
        plan["goal"]
    )

    execution = agent.execute(
        task["goal"]
    )

    runtime.update_status(
        task["task_id"],
        "completed",
        execution["result"]
    )

    feedback = monitor.monitor(
        task["goal"],
        execution["task"]
    )


    assert brain_result["goal"] == user_goal
    assert memory_result["importance_score"] == 1
    assert plan["status"] == "planned"
    assert execution["status"] == "completed"
    assert feedback["deviation"] is False


    print(
        "AI-OS Core MVP V1.3 PASS"
    )


if __name__ == "__main__":
    test_aios_core_mvp_v13()
