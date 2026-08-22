class SystemMonitor:


    def __init__(self):

        self.status = "running"


    def get_status(self):

        return {
            "status": self.status
        }


    def stop(self):

        self.status = "stopped"
