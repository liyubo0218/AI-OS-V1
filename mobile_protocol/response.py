class MobileResponse:


    def __init__(
        self,
        request_id,
        status,
        data
    ):

        self.request_id = request_id

        self.status = status

        self.data = data



    def to_dict(self):

        return {

            "request_id":
            self.request_id,

            "status":
            self.status,

            "data":
            self.data

        }
