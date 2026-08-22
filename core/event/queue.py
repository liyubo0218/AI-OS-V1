from collections import deque


class EventQueue:

    def __init__(self):

        self.queue = deque()


    def push(
        self,
        event
    ):

        self.queue.append(event)

        return {
            "status": "queued"
        }


    def pop(self):

        if not self.queue:

            return None

        return self.queue.popleft()


    def size(self):

        return len(self.queue)
