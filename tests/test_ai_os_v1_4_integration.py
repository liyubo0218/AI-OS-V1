from core.personal_memory_intelligence import (
    PreferenceAnalyzer,
    HabitTracker,
    UserProfileModel
)

from core.real_capability_execution import (
    ExecutionManager,
    CapabilityRouter
)

from core.autonomous_task_management import (
    TaskScheduler,
    TaskTracker,
    StatusPredictor,
    DeviationHandler
)


def test_ai_os_v1_4_integration():


    # 1. Personal Memory Intelligence

    analyzer = PreferenceAnalyzer()

    preference = analyzer.analyze(
        "喜欢高效率工作方式"
    )

    assert preference["identified"] is True



    tracker = HabitTracker()

    tracker.record(
        "每日检查任务"
    )

    assert len(
        tracker.list_habits()
    ) == 1



    profile = UserProfileModel()

    profile.update(
        "work_style",
        "efficient"
    )

    assert profile.get(
        "work_style"
    ) == "efficient"



    # 2. Real Capability Execution

    manager = ExecutionManager()

    router = CapabilityRouter()


    manager.register_executor(
        "computer",
        {
            "type": "computer_executor"
        }
    )


    route = router.route(
        "computer"
    )

    assert route["route"] == "execution"



    execution = manager.execute(
        "computer",
        {
            "action": "open_task"
        }
    )

    assert execution["status"] == "executed"



    # 3. Autonomous Task Management

    scheduler = TaskScheduler()

    task_tracker = TaskTracker()

    predictor = StatusPredictor()

    deviation = DeviationHandler()



    schedule = scheduler.schedule(
        "完成项目"
    )

    assert schedule["status"] == "scheduled"



    task_tracker.update(
        "001",
        80
    )


    status = predictor.predict(
        task_tracker.get("001")
    )


    assert status["status"] == "in_progress"



    action = deviation.handle(
        "delayed"
    )


    assert action["action"] == "remind"



    print(
        "AI-OS V1.4 INTEGRATION PASS"
    )



if __name__ == "__main__":

    test_ai_os_v1_4_integration()
