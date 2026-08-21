from core.memory.context_builder import ContextBuilder


class MemoryContextAdapter:

    def __init__(
        self,
        context_builder=None
    ):
        self.context_builder = (
            context_builder
            or ContextBuilder()
        )


    def get_memory_context(
        self,
        query
    ):

        try:
            result = self.context_builder.build_context(
                query
            )

            return {
                "memory_context":
                    result.get(
                        "context",
                        []
                    )
            }

        except Exception:

            return {
                "memory_context": []
            }
