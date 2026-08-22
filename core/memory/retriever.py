from .storage import MemoryStorage


class MemoryRetriever:
    """
    AI-OS 记忆检索层

    负责：
    - 根据需求查找相关记忆
    - 提供上下文信息

    不负责：
    - AI推理
    - 任务决策
    """

    def __init__(
        self,
        storage=None
    ):
        self.storage = storage or MemoryStorage()


    def search(
        self,
        keyword
    ):
        results = []

        memories = self.storage.all()

        for key, item in memories.items():

            text = str(
                item.get(
                    "value",
                    ""
                )
            )

            if keyword.lower() in text.lower():

                results.append(
                    {
                        "key": key,
                        "value": item.get(
                            "value"
                        )
                    }
                )

        return results


    def get_context(
        self,
        query
    ):
        return {
            "query": query,
            "memories": self.search(
                query
            )
        }


    def find_by_key(
        self,
        key
    ):
        return self.storage.get(
            key
        )


    def summarize(
        self,
        query
    ):
        memories = self.search(
            query
        )

        return {
            "count": len(memories),
            "items": memories
        }
