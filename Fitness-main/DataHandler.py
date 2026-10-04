from math import ceil

from Participant import Participant, Session
from ObservationValidator import ObservationValidator
from standaloneFunctions import calculate_summary

class DataHandler:
    def __init__(self, Participant: Participant, Session: Session, badRecords):
        self.participant = Participant
        self.session = Session
        self.observations = Session.observations
        self.badRecordsInt = self.badRecordsCounter(badRecords)
        
        summaries = self.average(self.observations)

        self.heart_rate_summary = summaries[0]
        self.skin_response_summary = summaries[1]
        self.temperature_summary = summaries[2]
        self.activity_level_summary = summaries[3]
        self.signal_quality_summary = summaries[4]
        
        #Now lets make two lists from observations
        #One with the first three values and one with the last three
        #This way we can see if the heart rate is recovering near the end
        middleNum = ceil(len(self.observations)/2)

        self.observationsBeginning = self.session.observations[:middleNum]
        self.observationsEnd = self.session.observations[-middleNum:]

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
            valid = False
            if("heart_rate" not in validate):
                heart_rates.append(observation["heart_rate"])
                valid = True
            if("skin_response" not in validate):
                skin_responses.append(observation["skin_response"])
                valid = True
            if("temperature" not in validate):
                temperatures.append(observation["temperature"])
                valid = True
            if("activity_level" not in validate):
                activity_levels.append(observation["activity_level"])
                valid = True
            if("signal_quality" not in validate):
                signal_qualities.append(observation["signal_quality"])
                valid = True
            if valid == True:
                i += 1

        heart_rate_summary = calculate_summary(heart_rates, i)
        skin_response_summary = calculate_summary(skin_responses, i)
        temperature_summary = calculate_summary(temperatures, i)
        activity_level_summary = calculate_summary(activity_levels, i)
        signal_quality_summary = calculate_summary(signal_qualities, i)

        return heart_rate_summary, skin_response_summary, temperature_summary, activity_level_summary, signal_quality_summary


    def badRecordsCounter(self, badRecords):
        counter = 0

        for row in badRecords:
            rowData = row[0]

            if rowData["session_id"] == self.session.sessionID:
                counter += 1

        return counter