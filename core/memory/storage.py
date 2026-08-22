class MemoryStorage:


    def __init__(self):

        self.data = {}


    def save(
        self,
        key,
        value
    ):

        self.data[key] = value

        return {
            "status": "saved"
        }


    def get(
        self,
        key
    ):

        return self.data.get(key)


    def delete(
        self,
        key
    ):

        if key in self.data:

            del self.data[key]

            return {
                "status": "deleted"
            }

        return {
            "status": "not_found"
        }
