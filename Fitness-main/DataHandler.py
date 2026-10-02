from Participant import Participant2
from ObservationValidator import ObservationValidator
from standaloneFunctions import calculate_summary

class DataHandler:
    def __init__(self, Participant: Participant2):
        self.participant = Participant
        self.observations = self.participant.observations
        self.heart_rate_summary, self.skin_response_summary, self.temperature_summary, self.activity_level_summary, self.signal_quality_summary = self.average(self.observations)

        #Now lets make two lists from observations
        #One with the first three values and one with the last three
        #This way we can see if the heart rate is recovering near the end
        middleNum = int(len(self.observations)/2)

        self.observationsBeginning = self.participant.observations[:middleNum]
        self.observationsEnd = self.participant.observations[-middleNum:]

        self.heart_rate_summaryBeginning = self.average(self.observationsBeginning)[0]
        self.heart_rate_summaryEnd = self.average(self.observationsEnd)[0]

        self.activity_level_summaryBeginning = self.average(self.observationsBeginning)[3]
        self.activity_level_summaryEnd = self.average(self.observationsEnd)[3]
        

    def average(self, observationList):
        heart_rates = []
        skin_responses = []
        temperatures = []
        activity_levels = []
        signal_qualities = []
        i = 0
        for observation in observationList:
            validate = ObservationValidator.validate(observation)
            if("heart_rate" not in validate):
                heart_rates.append(observation["heart_rate"])
            if("skin_response" not in validate):
                skin_responses.append(observation["skin_response"])
            if("temperature" not in validate):
                temperatures.append(observation["temperature"])
            if("activity_level" not in validate):
                activity_levels.append(observation["activity_level"])
            if("signal_quality" not in validate):
                signal_qualities.append(observation["signal_quality"])
            i += 1

        
        heart_rate_summary = calculate_summary(heart_rates, i)
        skin_response_summary = calculate_summary(skin_responses, i)
        temperature_summary = calculate_summary(temperatures, i)
        activity_level_summary = calculate_summary(activity_levels, i)
        signal_quality_summary = calculate_summary(signal_qualities, i)

        return heart_rate_summary, skin_response_summary, temperature_summary, activity_level_summary, signal_quality_summary


