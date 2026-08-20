from memory.memory_manager import MemoryManager


memory = MemoryManager()


result = memory.save_memory(
    "workflow_test_001",
    "task_history",
    "完成任务:Workflow Memory测试"
)


print("Workflow Memory Test Ready")

print(result)

print("All Memory:")

print(memory.get_all_memory())
