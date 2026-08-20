from mobile_protocol.request import MobileRequest
from mobile_gateway.protocol_handler import ProtocolHandler
from mobile_gateway.gateway import MobileGateway
from mobile_gateway.brain_adapter import BrainAdapter

from core.brain.brain import Brain
from core.brain.interface import BrainInterface


class MockSync:

    def receive_event(self, event):

        return {
            "sync": "ok"
        }


class MockOrchestrator:

    def run(self, text):

        return {
            "execute": text
        }


def test_mobile_brain_bridge():

    brain = Brain()

    brain_interface = BrainInterface(
        brain
    )

    brain_adapter = BrainAdapter(
        brain_interface
    )


    gateway = MobileGateway(
        MockOrchestrator(),
        MockSync(),
        brain_adapter
    )


    handler = ProtocolHandler(
        gateway
    )


    request = MobileRequest(
        "iphone_001",
        "session_001",
        "chat",
        {
            "text": "测试AI-OS"
        }
    )


    response = handler.handle(
        request
    )


    result = response.to_dict()


    assert result["request_id"] == "iphone_001"

    assert result["status"] == "success"

    assert result["data"]["brain"]["intent"] == "test_system"

    assert result["data"]["brain"]["goal"] == "测试AI-OS"


    print("Mobile Brain Bridge PASS")


if __name__ == "__main__":

    test_mobile_brain_bridge()
