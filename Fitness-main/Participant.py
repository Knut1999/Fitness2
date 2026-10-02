class Participant:
    def __init__(self, name, participant_id, scenario, seed, number_of_windows):
        self.name = name
        self.participant_id = participant_id
        self.scenario = scenario
        self.seed = seed
        self.number_of_windows = number_of_windows

        #fremtidig data
        self.profile = None
        self.observations = None

class Participant2:
    def __init__(self, name, participant_id, baseline_heart_rate, baseline_skin_response, baseline_temperature):
        self.baseline_heart_rate = baseline_heart_rate
        self.baseline_skin_response = baseline_skin_response
        self.baseline_temperature = baseline_temperature
        self.name = name
        self.participant_id = participant_id

        #fremtidig data
        self.profile = {'participant_id': self.participant_id, 
                        'baseline_heart_rate': self.baseline_heart_rate, 
                        'baseline_skin_response': self.baseline_skin_response, 
                        'baseline_temperature': self.baseline_temperature}

        "Observation containing session ID, timestamp, heart rate, skin response, temperature, activity level, and signal quality."
        self.observations = []


