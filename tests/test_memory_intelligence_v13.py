from core.memory.intelligence.memory_intelligence import MemoryIntelligence


def test_memory_intelligence_v13():

    memory = MemoryIntelligence()

    result = memory.analyze(
        "用户喜欢早上查看任务"
    )

    assert len(result["memory_items"]) == 1

    assert result["memory_items"][0]["content"] == "用户喜欢早上查看任务"

    assert result["importance_score"] == 1

    assert result["context_summary"] == "用户喜欢早上查看任务"

    print(
        "Memory Intelligence V1.3 PASS"
    )


if __name__ == "__main__":
    test_memory_intelligence_v13()
