from memory.memory_manager import MemoryManager


memory = MemoryManager()


saved = memory.save_memory(
    "memory_task_001",
    "task_history",
    "完成任务:帮我测试AI-OS"
)


print("Memory Manager V2 Ready")


print("Saved:")

print(saved)


print("All Memory:")

print(
    memory.get_all_memory()
)


print("Search:")

print(
    memory.search_memory(
        "AI-OS"
    )
)
