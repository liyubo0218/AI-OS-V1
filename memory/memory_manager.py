from memory.storage import MemoryStorage


class MemoryManager:

    def __init__(self):

        self.storage = MemoryStorage()


    def save_memory(
        self,
        memory_id,
        memory_type,
        content
    ):

        self.storage.save(
            memory_id,
            memory_type,
            content
        )


        return {
            "memory_id": memory_id,
            "type": memory_type,
            "content": content
        }


    def get_all_memory(self):

        return self.storage.get_all()


    def search_memory(
        self,
        keyword
    ):

        memories = self.storage.get_all()


        return [
            memory
            for memory in memories
            if keyword in memory["content"]
        ]
