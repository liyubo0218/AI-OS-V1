from core.memory import MemoryManager


def test_memory():

    memory = MemoryManager()


    memory.save_user(
        "001",
        {
            "name": "user"
        }
    )


    result = memory.get_user(
        "001"
    )


    assert result["name"] == "user"


    print(
        "Memory Manager PASS"
    )


if __name__ == "__main__":

    test_memory()
