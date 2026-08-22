from core.system import (
    ConfigManager,
    Logger,
    SystemMonitor
)


def test_system():


    config = ConfigManager()

    config.set(
        "mode",
        "mvp"
    )


    assert config.get(
        "mode"
    ) == "mvp"


    logger = Logger()

    logger.write(
        "test"
    )


    monitor = SystemMonitor()

    assert monitor.get_status()["status"] == "running"


    print(
        "System Support PASS"
    )


if __name__ == "__main__":

    test_system()
