class RetryManager:


    def __init__(
        self,
        max_retry=3
    ):

        self.max_retry = max_retry



    def should_retry(
        self,
        count
    ):

        return count < self.max_retry
