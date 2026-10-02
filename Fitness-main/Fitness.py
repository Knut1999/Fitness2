from DataHandler import DataHandler
from Participant import Participant2
from GenerateReport import GenerateReport
from SessionClassifyer import SessionClassifyer
from standaloneFunctions import findParticipantData


class Fitness:
    def __init__(self, participants: dict[str, Participant2]):
        self.participants = participants
        self.badRecords = []

        #this function reads from csv, finds invalid ids, and gives the session timestamps to the correct participant
        findParticipantData(self, "./fitness/Fitness-main/data/fitness_sessions.csv")
        # findParticipantData(self, "./fitness/Fitness-main/data/fitness_sessions_invalid.csv")


        #We first get the data from the fitness tracker
        i = 0
        for id, participant in self.participants.items():
            # Now we need to handle the data
            dataHandler = DataHandler(participant)
            # sessionClassifyer = SessionClassifyer(dataHandler) 

            # # # Generate report
            # # i += 1
            # # generateReport = GenerateReport(dataHandler, sessionClassifyer, i)

            # # print(generateReport)