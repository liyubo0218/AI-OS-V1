class AIOSSettings:


    def __init__(self):

        # 系统信息

        self.name = "AI-OS"

        self.version = "V1.0"



        # AI模式

        self.ai_mode = "mock"



        # Device配置

        self.default_device = "iphone_001"



        # Runtime状态

        self.environment = "development"



        # 日志

        self.log_level = "INFO"



    def to_dict(
        self
    ):

        return {

            "name":
            self.name,

            "version":
            self.version,

            "ai_mode":
            self.ai_mode,

            "default_device":
            self.default_device,

            "environment":
            self.environment,

            "log_level":
            self.log_level

        }
