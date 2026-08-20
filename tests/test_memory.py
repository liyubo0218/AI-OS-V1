from memory.memory_manager import MemoryManager


memory_manager = MemoryManager()


memory = {
    "memory_id": "memory_001",
    "type": "project_info",
    "content": "用户正在开发AI-OS项目"
}


memory_manager.save_memory(
    memory
)


print("Memory Saved")


result = memory_manager.retrieve_memory(
    "AI-OS"
)


print("Memory Retrieved:")

print(result)


print("All Memory:")

print(
    memory_manager.list_memory()
)
