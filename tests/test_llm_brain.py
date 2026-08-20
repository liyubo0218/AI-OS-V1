from core.brain.brain import Brain
from core.brain.llm_gateway import LLMGateway
from core.brain.model_adapter import MockModelAdapter


def test_llm_brain():

    gateway = LLMGateway(
        MockModelAdapter()
    )


    brain = Brain(
        gateway
    )


    rule_result = brain.understand(
        {
            "user_input":"测试AI-OS"
        }
    )


    assert rule_result["intent"] == "test_system"


    llm_result = brain.understand(
        {
            "user_input":"帮我规划一个复杂任务"
        }
    )


    assert llm_result["intent"] == "llm_reasoning"


    print("LLM Brain PASS")


if __name__ == "__main__":

    test_llm_brain()
