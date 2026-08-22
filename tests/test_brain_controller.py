from core.brain import BrainController


def test_brain_controller():

    brain = BrainController()

    result = brain.process(
        "测试任务"
    )


    assert result["status"] == "received"

    assert result["final_state"] == "completed"


    print(
        "Brain Controller PASS"
    )


if __name__ == "__main__":

    test_brain_controller()
