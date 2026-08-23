from .capability import Capability
from .result import MobileResult


class MobileAgent:
    """
    AI-OS Mobile Agent

    负责：
    - 管理手机能力
    - 转换动作
    - 调用手机网关
    - 返回统一结果

    不负责：
    - AI推理
    - 任务规划
    - 底层设备控制
    """

    def __init__(
        self,
        action_mapper=None,
        gateway=None
    ):
        self.action_mapper = action_mapper
        self.gateway = gateway


    def discover_capabilities(
        self
    ):
        return [
            Capability(
                "shortcut",
                "shortcut"
            ).to_dict(),

            Capability(
                "notification",
                "notification"
            ).to_dict(),

            Capability(
                "device",
                "device"
            ).to_dict()
        ]


    def execute(
        self,
        action,
        payload=None
    ):
        if not self.action_mapper:
            return MobileResult(
                "failed",
                action,
                {
                    "error":"mapper_unavailable"
                }
            ).to_dict()

        mapped = self.action_mapper.map_action(
            action,
            payload
        )

        if not self.gateway:
            return MobileResult(
                "failed",
                action,
                {
                    "error":"gateway_unavailable"
                }
            ).to_dict()

        result = self.gateway.execute(
            mapped
        )

        return MobileResult(
            "success",
            action,
            result
        ).to_dict()
