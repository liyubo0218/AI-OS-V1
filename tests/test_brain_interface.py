from core.brain.brain import Brain
from core.brain.interface import BrainInterface
from core.brain.request import BrainRequest


def test_brain_interface():

    brain = Brain()

    interface = BrainInterface(
        brain
    )

    request = BrainRequest(
        request_id="req_001",
        user_input="测试AI-OS",
        source="iphone"
    )

    response = interface.process(
        request
    )

    result = response.to_dict()

    assert result["request_id"] == "req_001"
    assert result["intent"] == "test_system"
    assert result["goal"] == "测试AI-OS"
    assert result["confidence"] == 0.95

    print("Brain Interface PASS")


if __name__ == "__main__":

    test_brain_interface()
