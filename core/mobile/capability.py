class Capability:
    """
    AI-OS Mobile Capability

    负责：
    - 描述设备能力
    - 提供能力信息

    不负责：
    - 执行动作
    - 设备控制
    """

    def __init__(
        self,
        name,
        channel,
        available=True
    ):
        self.name = name
        self.channel = channel
        self.available = available


    def to_dict(
        self
    ):
        return {
            "name": self.name,
            "channel": self.channel,
            "available": self.available
        }
