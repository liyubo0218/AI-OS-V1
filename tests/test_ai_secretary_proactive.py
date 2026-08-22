from core.ai_secretary_proactive import (
    ReminderEngine,
    SuggestionEngine,
    RiskDetector,
    ScheduleCoordinator
)



def test_ai_secretary_proactive():


    reminder = ReminderEngine()

    suggestion = SuggestionEngine()

    risk = RiskDetector()

    schedule = ScheduleCoordinator()



    result = reminder.create(
        "完成项目"
    )

    assert result["reminder"] == "created"



    result = suggestion.suggest(
        "工作任务"
    )

    assert result["suggestion"] == "recommended"



    result = risk.detect(
        "delayed"
    )

    assert result["risk"] is True



    result = schedule.coordinate(
        [
            "meeting",
            "task"
        ]
    )

    assert result["status"] == "coordinated"



    print(
        "AI Secretary Proactive Layer PASS"
    )



if __name__ == "__main__":

    test_ai_secretary_proactive()
