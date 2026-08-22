class PermissionController:


    def __init__(self):

        self.permissions = {}



    def grant(
        self,
        name,
        permission
    ):

        self.permissions[name] = permission


        return {
            "status": "granted"
        }



    def check(
        self,
        name
    ):

        return name in self.permissions
