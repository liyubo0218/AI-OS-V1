class OfflineQueue:


    def __init__(self):

        self.queue = []



    def add(
        self,
        event
    ):

        self.queue.append(
            event
        )


        return {
            "status":"queued"
        }



    def get_all(
        self
    ):

        return self.queue



    def remove(
        self,
        event
    ):

        if event in self.queue:

            self.queue.remove(
                event
            )


        return {
            "status":"removed"
        }



    def size(
        self
    ):

        return len(
            self.queue
        )
