from datetime import datetime


class Logger:


    def __init__(self):

        self.logs = []


    def write(
        self,
        message
    ):

        self.logs.append(
            {
                "time": datetime.utcnow().isoformat(),
                "message": message
            }
        )


    def get_logs(self):

        return self.logs
