from session.session import Session



class SessionManager:


    def __init__(
        self
    ):

        self.sessions = {}



    def create_session(
        self,
        session_id,
        device_id
    ):


        session = Session(

            session_id,

            device_id

        )


        self.sessions[session_id] = session


        return session.to_dict()



    def open_session(
        self,
        session_id
    ):


        session = self.sessions.get(
            session_id
        )


        if session:

            session.activate()

            return session.to_dict()



        return None



    def close_session(
        self,
        session_id
    ):


        session = self.sessions.get(
            session_id
        )


        if session:

            session.close()

            return session.to_dict()



        return None



    def get_session(
        self,
        session_id
    ):


        session = self.sessions.get(
            session_id
        )


        return (

            session.to_dict()

            if session

            else None

        )

