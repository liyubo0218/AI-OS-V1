from config.settings import AIOSSettings

from logging.logger import AIOSLogger

from runtime.manager import RuntimeManager

from sync.gateway import SyncGateway

from device.registry import DeviceRegistry



print(
    "===== AI-OS V1.0 RC1 Health Check ====="
)



results = []



# Config Check

try:

    settings = AIOSSettings()

    print(
        "Config: PASS"
    )

    results.append(True)


except Exception:

    print(
        "Config: FAIL"
    )

    results.append(False)



# Logger Check

try:

    logger = AIOSLogger()

    logger.info(
        "Health Check"
    )

    print(
        "Logger: PASS"
    )

    results.append(True)


except Exception:

    print(
        "Logger: FAIL"
    )

    results.append(False)



# Runtime Check

try:

    runtime = RuntimeManager()

    runtime.start()

    print(
        "Runtime: PASS"
    )

    results.append(True)


except Exception:

    print(
        "Runtime: FAIL"
    )

    results.append(False)



# Sync Check

try:

    sync = SyncGateway()

    print(
        "Sync: PASS"
    )

    results.append(True)


except Exception:

    print(
        "Sync: FAIL"
    )

    results.append(False)



# Device Check

try:

    device = DeviceRegistry()

    print(
        "Device: PASS"
    )

    results.append(True)


except Exception:

    print(
        "Device: FAIL"
    )

    results.append(False)



print()



if all(results):

    print(
        "SYSTEM READY"
    )


else:

    print(
        "SYSTEM ERROR"
    )

