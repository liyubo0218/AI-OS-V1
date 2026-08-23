from datetime import datetime
import uuid


class MemoryRecord:
    """
    AI-OS Memory 统一记忆对象
    """

    def __init__(
        self,
        memory_type,
        content,
        importance=0.5
    ):
        self.id = str(uuid.uuid4())
        self.type = memory_type
        self.content = content
        self.importance = importance
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "content": self.content,
            "importance": self.importance,
            "created_at": self.created_at.isoformat()
        }
