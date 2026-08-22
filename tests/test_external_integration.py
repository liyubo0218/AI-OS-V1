from core.external_integration import (
    ServiceManager,
    ServiceExecutor,
    ServiceFeedback
)


def test_external_integration():


    manager = ServiceManager()

    executor = ServiceExecutor()

    feedback = ServiceFeedback()



    manager.add_service(
        "calendar",
        {
            "type": "schedule"
        }
    )


    service = manager.get_service(
        "calendar"
    )


    assert service is not None



    result = executor.execute(
        service,
        {
            "action": "create_event"
        }
    )


    assert result["status"] == "executed"



    feedback.record(
        result
    )


    assert feedback.latest() == result



    print(
        "External Service Integration Layer PASS"
    )


if __name__ == "__main__":

    test_external_integration()
