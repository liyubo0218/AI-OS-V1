from core.multi_device_intelligence import (
    DeviceState,
    CapabilityMapper,
    DeviceSelector,
    TaskRouter,
    SyncManager
)

from core.advanced_user_model import (
    PreferenceModel,
    BehaviorAnalyzer,
    DecisionPattern,
    PersonalStrategy
)

from core.ai_secretary_proactive import (
    ReminderEngine,
    SuggestionEngine,
    RiskDetector,
    ScheduleCoordinator
)


def test_ai_os_v1_5_integration():


    # 1. Multi Device Intelligence

    state = DeviceState()

    mapper = CapabilityMapper()

    selector = DeviceSelector()

    router = TaskRouter()

    sync = SyncManager()


    state.update(
        "phone",
        "online"
    )

    assert state.get(
        "phone"
    ) == "online"


    mapper.register(
        "computer",
        [
            "file_operation"
        ]
    )


    device = selector.select(
        [
            {
                "name": "computer",
                "capabilities": [
                    "file_operation"
                ]
            }
        ],
        "file_operation"
    )


    assert device == "computer"


    route = router.route(
        "transfer_file",
        device
    )

    assert route["status"] == "routed"


    result = sync.sync(
        "transfer_file",
        "completed"
    )

    assert result["status"] == "synced"



    # 2. Advanced User Model

    preference = PreferenceModel()

    preference.update(
        "work_style",
        "efficient"
    )


    assert preference.get(
        "work_style"
    ) == "efficient"


    analyzer = BehaviorAnalyzer()

    behavior = analyzer.analyze(
        [
            "plan",
            "execute"
        ]
    )


    assert behavior["pattern"] == "identified"


    decision = DecisionPattern()

    decision.record(
        "compare_before_action"
    )


    assert len(
        decision.list_patterns()
    ) == 1


    strategy = PersonalStrategy()

    assert strategy.select(
        "task"
    )["strategy"] == "personalized"



    # 3. AI Secretary Proactive

    reminder = ReminderEngine()

    suggestion = SuggestionEngine()

    risk = RiskDetector()

    schedule = ScheduleCoordinator()


    assert reminder.create(
        "finish project"
    )["reminder"] == "created"


    assert suggestion.suggest(
        "work"
    )["suggestion"] == "recommended"


    assert risk.detect(
        "delayed"
    )["risk"] is True


    assert schedule.coordinate(
        [
            "meeting"
        ]
    )["status"] == "coordinated"



    print(
        "AI-OS V1.5 INTEGRATION PASS"
    )


if __name__ == "__main__":

    test_ai_os_v1_5_integration()
