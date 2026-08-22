from core.brain.context.brain_adapter import BrainAdapter
from core.memory_v2 import MemoryEngine
from core.planner import Planner
from core.executor import Executor
from core.goal_v2 import ActiveGoalMonitor


def test_ai_os_v1_1_integration():


    # 1. AI Brain Enhancement

    brain = BrainAdapter()

    understanding = brain.understand(
        "提醒我明天完成项目报告"
    )


    assert understanding["intent"] == "reminder"



    # 2. Memory 2.0

    memory = MemoryEngine()


    memory.save_preference(
        "user001",
        {
            "style": "simple"
        }
    )


    memory.save_history(
        {
            "task": "project report",
            "status": "pending"
        }
    )


    result = memory.search(
        "project"
    )


    assert len(result) == 1



    # 3. Planner

    planner = Planner()


    plan = planner.create_plan(
        "提醒我明天完成项目报告"
    )


    assert len(
        plan["workflow"]["steps"]
    ) > 0



    # 4. Executor

    executor = Executor()


    executor.register_action(
        "reminder",
        lambda x: {
            "executed": True
        }
    )


    execute_result = executor.execute(
        "reminder"
    )


    assert execute_result["executed"] is True



    # 5. Active Goal Monitor

    monitor = ActiveGoalMonitor()


    monitor.create_goal(
        "001",
        "完成项目报告"
    )


    monitor.tracker.update_progress(
        "001",
        50
    )


    status = monitor.monitor_goal(
        "001"
    )


    assert status["deviation"]["deviation"] is False



    print(
        "AI-OS V1.1 INTEGRATION PASS"
    )


if __name__ == "__main__":

    test_ai_os_v1_1_integration()
