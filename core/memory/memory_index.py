class MemoryIndex:
    """
    AI-OS Memory 索引层

    负责：
    - 建立记忆索引
    - 根据关键词检索相关记忆

    不负责：
    - AI推理
    - 数据持久化
    - 自动学习
    """

    def __init__(
        self
    ):
        self.index = []


    def add(
        self,
        category,
        keyword,
        content
    ):
        item = {
            "category": category,
            "keyword": keyword,
            "content": content
        }

        self.index.append(
            item
        )

        return True


    def search(
        self,
        query
    ):
        results = []

        for item in self.index:
            keyword = item.get(
                "keyword",
                ""
            )

            content = item.get(
                "content",
                ""
            )

            if (
                query in keyword
                or query in content
            ):
                results.append(
                    item
                )

        return results


    def all_items(
        self
    ):
        return self.index
