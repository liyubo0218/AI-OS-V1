from core.memory_v2 import MemoryEngine


def test_memory_v2():


    memory = MemoryEngine()


    memory.save_preference(
        "user001",
        {
            "style": "simple"
        }
    )


    preference = memory.get_preference(
        "user001"
    )


    assert preference["style"] == "simple"



    memory.save_history(
        {
            "task": "meeting reminder",
            "result": "completed"
        }
    )


    result = memory.search(
        "meeting"
    )


    assert len(result) == 1


    print(
        "Memory 2.0 PASS"
    )


if __name__ == "__main__":

    test_memory_v2()
