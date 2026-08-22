class ComputerPermissionManager:

    def __init__(self):
        self.permissions = {}


    def grant(
        self,
        permission
    ):

        self.permissions[permission] = True

        return {
            "status": "approved"
        }


    def validate(
        self,
        permission
    ):

        return {
            "authorized":
                self.permissions.get(
                    permission,
                    False
                )
        }


    def revoke(
        self,
        permission
    ):

        self.permissions[permission] = False

        return {
            "status": "revoked"
        }
