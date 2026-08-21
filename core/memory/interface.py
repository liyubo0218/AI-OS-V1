from memory.memory_manager import MemoryManager


class MemoryInterface:

    def __init__(
        self,
        manager=None
    ):

        self.manager = (
            manager
            or
            MemoryManager()
        )


    def save(
        self,
        memory_id,
        memory_type,
        content
    ):

        return self.manager.save_memory(
            memory_id,
            memory_type,
            content
        )


    def retrieve(self):

        return self.manager.get_all_memory()


    def search(
        self,
        keyword
    ):

        return self.manager.search_memory(
            keyword
        )


    def build_context(
        self,
        keyword=None
    ):

        if keyword:

            memories = self.search(
                keyword
            )

        else:

            memories = self.retrieve()


        return {
            "memories": memories
        }
