from core.memory_intelligence.memory_manager import (
    MemoryIntelligenceManager
)


class MockBrain:

    def request_context(
        self,
        memory_manager,
        query
    ):
        return memory_manager.retrieve_context(
            query
        )


def test_memory_intelligence_integration_v2():

    memory_manager = MemoryIntelligenceManager()

    brain = MockBrain()


    memory_manager.write_memory(
        "preference",
        "meeting_style",
        "提前准备会议",
        "user_interaction"
    )


    memory_manager.write_memory(
        "task_history",
        "previous_task",
        "会议资料整理完成",
        "task_result"
    )


    context = brain.request_context(
        memory_manager,
        "会议"
    )


    assert context["status"] == "completed"

    assert "提前准备会议" in context["context"]

    assert "会议资料整理完成" in context["context"]


    print(
        "Memory Intelligence Integration V2 PASS"
    )


if __name__ == "__main__":
    test_memory_intelligence_integration_v2()
