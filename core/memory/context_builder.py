from core.memory.interface import MemoryInterface


class ContextBuilder:

    def __init__(
        self,
        memory=None
    ):

        self.memory = (
            memory
            or
            MemoryInterface()
        )


    def build_context(
        self,
        query=None
    ):

        if query:

            memories = self.memory.search(
                query
            )

        else:

            memories = self.memory.retrieve()


        return {
            "context": memories
        }
