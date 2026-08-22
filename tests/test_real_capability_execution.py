from core.real_capability_execution import (
    ExecutionManager,
    CapabilityRouter
)



def test_real_capability_execution():


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



    result = manager.execute(
        "computer",
        {
            "action": "open_app"
        }
    )


    assert result["status"] == "executed"



    print(
        "Real Capability Execution Layer PASS"
    )



if __name__ == "__main__":

    test_real_capability_execution()
