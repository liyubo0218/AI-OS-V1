import json
import os


class SyncStorage:


    def __init__(
        self,
        path="sync_events.json"
    ):

        self.path = path



    def save(
        self,
        events
    ):

        with open(
            self.path,
            "w"
        ) as f:

            json.dump(
                events,
                f
            )



    def load(
        self
    ):


        if not os.path.exists(
            self.path
        ):

            return []


        with open(
            self.path,
            "r"
        ) as f:

            return json.load(
                f
            )

