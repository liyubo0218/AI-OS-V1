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


    # Rule Engine test

    rule_result = brain.understand(
        {
            "user_input":
            "测试AI-OS"
        }
    )


    assert rule_result["intent"] == "test_system"

    assert rule_result["confidence"] == 0.95



    # LLM fallback test

    llm_result = brain.understand(
        {
            "user_input":
            "帮我规划一个复杂任务"
        }
    )


    assert llm_result["intent"] == "llm_reasoning"

    assert llm_result["llm_response"]["model"] == "mock-llm"


    print("LLM Brain PASS")


if __name__ == "__main__":

    test_llm_brain()
