from Participant import Participant2
from GenerateReport import GenerateReport
from SessionClassifyer import SessionClassifyer
from standaloneFunctions import findParticipantData


class Fitness:
    def __init__(self, participants: list[Participant2]):
        self.participants = participants
        self.badRecords = []
        dataCSVReader = findParticipantData(self, participants, "./fitness/Fitness-main/data/fitness_sessions.csv")

        #We first get the data from the fitness tracker
        i = 0
        for participant in self.participants:
            pass
            # # Now we need to handle the data
            # dataHandler = DataHandler(participant)
            # sessionClassifyer = SessionClassifyer(dataHandler) 

            # # Generate report
            # i += 1
            # generateReport = GenerateReport(dataHandler, sessionClassifyer, i)

            # print(generateReport)