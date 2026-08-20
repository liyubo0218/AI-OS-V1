from local_runtime.local_cache import LocalCache

from local_runtime.offline_queue import OfflineQueue



class LocalRuntime:


    def __init__(
        self,
        device_agent
    ):

        self.device_agent = device_agent

        self.cache = LocalCache()

        self.queue = OfflineQueue()



    def run_local_task(
        self,
        command
    ):

        result = self.device_agent.execute(
            command
        )


        self.cache.save(
            command,
            result
        )


        return result



    def queue_cloud_task(
        self,
        event
    ):

        return self.queue.add(
            event
        )
