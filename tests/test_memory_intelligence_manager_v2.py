from core.memory_intelligence.memory_manager import (
    MemoryIntelligenceManager
)


def test_memory_intelligence_manager_v2():

    manager = MemoryIntelligenceManager()


    result = manager.write_memory(
        "preference",
        "meeting_style",
        "提前准备会议",
        "user_interaction"
    )


    assert result["status"] == "stored"


    context = manager.retrieve_context(
        "会议"
    )


    assert context["status"] == "completed"
    assert "提前准备会议" in context["context"]


    update = manager.update_memory(
        result["memory_id"],
        {
            "value": "提前一天准备会议"
        }
    )


    assert update["status"] == "updated"


    delete = manager.delete_memory(
        result["memory_id"]
    )


    assert delete["status"] == "deleted"


    print(
        "Memory Intelligence Manager V2 PASS"
    )


if __name__ == "__main__":
    test_memory_intelligence_manager_v2()
