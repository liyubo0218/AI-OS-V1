class MemoryIntelligenceManager:

    def __init__(self):
        self.memories = {}
        self.counter = 0


    def write_memory(
        self,
        memory_type,
        key,
        value,
        source
    ):
        self.counter += 1

        memory_id = f"memory_{self.counter:03d}"

        self.memories[memory_id] = {
            "memory_type": memory_type,
            "key": key,
            "value": value,
            "source": source
        }

        return {
            "status": "stored",
            "memory_id": memory_id
        }


    def retrieve_context(
        self,
        query
    ):
        results = []

        for memory in self.memories.values():

            if (
                query in memory["value"]
                or query in memory["key"]
            ):
                results.append(
                    memory["value"]
                )

        return {
            "status": "completed",
            "context": results
        }


    def update_memory(
        self,
        memory_id,
        update
    ):
        if memory_id not in self.memories:
            return {
                "status": "failed"
            }

        self.memories[memory_id].update(
            update
        )

        return {
            "status": "updated"
        }


    def delete_memory(
        self,
        memory_id
    ):
        if memory_id in self.memories:
            del self.memories[memory_id]

        return {
            "status": "deleted"
        }
