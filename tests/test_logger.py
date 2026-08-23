from core.system.logger import Logger


def test_logger_write():

    logger = Logger()

    logger.write(
        "AI-OS started"
    )

    logs = logger.get_logs()

    assert len(logs) == 1

    assert (
        logs[0]["message"]
        == "AI-OS started"
    )


def test_logger_multiple_logs():

    logger = Logger()

    logger.write(
        "request received"
    )

    logger.write(
        "task created"
    )

    logs = logger.get_logs()

    assert len(logs) == 2

    assert (
        "time" in logs[0]
    )

    assert (
        "message" in logs[1]
    )
