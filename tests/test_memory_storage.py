from memory.storage import MemoryStorage


storage = MemoryStorage()


storage.save(
    "memory_001",
    "task_history",
    "完成任务:测试AI-OS"
)


print("Memory Storage Ready")


print(
    storage.get_all()
)
