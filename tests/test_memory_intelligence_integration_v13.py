from core.memory.intelligence.memory_intelligence import MemoryIntelligence


class MockContextBuilder:

    def build(self, memory_result):
        return {
            "context_ready": True,
            "summary": memory_result["context_summary"]
        }


def test_memory_intelligence_integration_v13():

    memory = MemoryIntelligence()

    context_builder = MockContextBuilder()

    memory_result = memory.analyze(
        "用户习惯晚上整理任务"
    )

    context_result = context_builder.build(
        memory_result
    )

    assert memory_result["importance_score"] == 1

    assert context_result["context_ready"] is True

    assert context_result["summary"] == "用户习惯晚上整理任务"

    print(
        "Memory Intelligence Integration V1.3 PASS"
    )


if __name__ == "__main__":
    test_memory_intelligence_integration_v13()
