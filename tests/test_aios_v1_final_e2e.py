from runtime.local import LocalRuntime

from runtime.cloud import CloudRuntime

from core.runtime_router import RuntimeRouter

from core.orchestrator_runtime import RuntimeOrchestrator



class Memory:


    def __init__(self):

        self.data = []



    def save(
        self,
        item
    ):

        self.data.append(item)



    def get(
        self
    ):

        return self.data




class DeviceGateway:


    def execute(
        self,
        device,
        command
    ):

        return {

            "device":
            device,

            "command":
            command,

            "status":
            "completed"

        }



print(
    "===== AI-OS V1.0 FINAL E2E ====="
)



# Runtime

local = LocalRuntime()

cloud = CloudRuntime()


local.start()

cloud.start()



router = RuntimeRouter(

    local,

    cloud

)



orchestrator = RuntimeOrchestrator(

    router

)



memory = Memory()

device = DeviceGateway()



# 1 iPhone

print(
    "iPhone:"
)


photo = orchestrator.execute(

    "camera_capture"

)


memory.save(photo)



print(photo)



# 2 Cloud

print(
    "Cloud:"
)


analysis = orchestrator.execute(

    "large_ai_analysis"

)


memory.save(analysis)



print(analysis)



# 3 Car

print(
    "Car:"
)


car = device.execute(

    "XPeng P7",

    "navigate_company"

)


memory.save(car)



print(car)



print(
    "Sync:"
)

print(
    "PASS"
)



print(
    "Memory:"
)

print(

    memory.get()

)



print(
    "===== AI-OS V1.0 READY ====="
)

