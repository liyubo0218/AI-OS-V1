from session.device_session import DeviceSession

from session.sync_session import SyncSession



class SessionManager:


    def __init__(self):

        self.sessions = {}



    def create_session(
        self,
        session_id,
        device_id
    ):

        session = {

            "sync":
            SyncSession(
                session_id
            ),

            "device":
            DeviceSession(
                device_id
            )

        }


        self.sessions[session_id] = session


        return {
            "status":"created",
            "session_id":session_id
        }



    def connect_device(
        self,
        session_id
    ):

        session = self.sessions[session_id]


        session["sync"].activate()


        return session["device"].connect()



    def disconnect_device(
        self,
        session_id
    ):

        session = self.sessions[session_id]


        return session["device"].disconnect()
