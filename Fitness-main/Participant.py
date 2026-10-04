class Participant:
    def __init__(self, name, participant_id, baseline_heart_rate, baseline_skin_response, baseline_temperature):
        self.sessions = [] 
        self.baseline_heart_rate = baseline_heart_rate
        self.baseline_skin_response = baseline_skin_response
        self.baseline_temperature = baseline_temperature
        self.name = name
        self.participant_id = participant_id

        self.profile = {'participant_id': self.participant_id, 
                        'baseline_heart_rate': float(self.baseline_heart_rate), 
                        'baseline_skin_response': float(self.baseline_skin_response), 
                        'baseline_temperature': float(self.baseline_temperature)}

        #fremtidig data
        self.observations = []


    def createSessions(self):
        current_session_id = None
        session_observations = []

        for observation in self.observations:
            #First row
            if current_session_id == None:
                current_session_id = observation["session_id"]
                session_observations.append(observation)
                continue

            #if this row is same as before add to session observations
            if current_session_id == observation["session_id"]:
                session_observations.append(observation)

            if current_session_id != observation["session_id"]:
                #this row is a new session, so we create session object from erlier observations
                session = Session(current_session_id, session_observations)
                self.sessions.append(session)
                #now we have createt a session, now we deal wit current row
                session_observations = []
                session_observations.append(observation)
                current_session_id = observation["session_id"]

        #and of course lets make the last session
        session = Session(current_session_id, session_observations)
        self.sessions.append(session)



class Session:
    def __init__(self, sessionId, observations):
        self.sessionID = sessionId
        self.observations = observations