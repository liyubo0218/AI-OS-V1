from core.autonomous_task_management import (
    TaskScheduler,
    TaskTracker,
    StatusPredictor,
    DeviationHandler
)



def test_autonomous_task_management():


    scheduler = TaskScheduler()

    tracker = TaskTracker()

    predictor = StatusPredictor()

    handler = DeviationHandler()



    result = scheduler.schedule(
        "完成项目"
    )


    assert result["status"] == "scheduled"



    tracker.update(
        "001",
        50
    )


    progress = tracker.get(
        "001"
    )


    assert progress == 50



    status = predictor.predict(
        progress
    )


    assert status["status"] == "in_progress"



    action = handler.handle(
        "delayed"
    )


    assert action["action"] == "remind"



    print(
        "Autonomous Task Management Layer PASS"
    )



if __name__ == "__main__":

    test_autonomous_task_management()
