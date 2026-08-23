class ConfigManager:
    """
    AI-OS Config Manager

    负责：
    - 管理运行配置
    - 提供配置访问

    不负责：
    - 配置文件加载
    - 环境管理
    """

    def __init__(
        self
    ):
        self.config = {}


    def set(
        self,
        key,
        value
    ):
        self.config[key] = value


    def get(
        self,
        key,
        default=None
    ):
        return self.config.get(
            key,
            default
        )


    def load(
        self,
        data
    ):
        self.config.update(
            data
        )


    def all(
        self
    ):
        return self.config
