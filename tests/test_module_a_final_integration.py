from core.brain.brain import Brain
from core.brain.llm_gateway import LLMGateway
from core.brain.model_router import ModelRouter
from core.brain.providers.real_provider import RealProvider
from memory.memory_manager import MemoryManager


def test_module_a_final_integration():

    provider = RealProvider()

    router = ModelRouter(
        provider
    )

    gateway = LLMGateway(
        router
    )

    brain = Brain(
        gateway
    )


    result = brain.understand(
        {
            "user_input":
            "帮我分析一个复杂任务"
        }
    )


    assert (
        result["intent"]
        ==
        "llm_reasoning"
    )


    memory = MemoryManager()

    saved = memory.save_memory(
        "memory_module_a_test",
        "task_history",
        "Module A integration test"
    )


    assert saved is not None


    print(
        "Module A Final Integration PASS"
    )


if __name__ == "__main__":

    test_module_a_final_integration()
