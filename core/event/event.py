from datetime import datetime
import uuid


class Event:
    """
    AI-OS Event v2 事件对象

    负责：
    - 保存事件信息
    - 标准化事件结构

    不负责：
    - 事件分发
    - 事件存储
    """

    def __init__(
        self,
        event_type,
        payload=None
    ):
        self.event_id = str(
            uuid.uuid4()
        )

        self.event_type = event_type

        self.payload = (
            payload
            if payload is not None
            else {}
        )

        self.timestamp = datetime.utcnow()


    def to_dict(
        self
    ):
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "payload": self.payload,
            "timestamp":
                self.timestamp.isoformat()
        }
