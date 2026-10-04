from DataHandler import DataHandler
from Participant import Participant
from ReportInterface import ReportInterface
from Report import GenerateValidReport, GenerateErrorReport, GenerateSummaryReport
from SessionClassifyer import SessionClassifyer
from standaloneFunctions import csvDataToList, assign_rows_to_participants, rowValidator


class Fitness:
    def __init__(self, participants: list[Participant]):
        self.participants = participants
        self.badRecords = []
        self.rows = []
        #this function creates a list with the csv data, it checks for errors with regex
        try:
            self.rows.extend(csvDataToList(self, "./Fitness2/Fitness-main/data/fitness_sessions.csv"))
            self.rows.extend(csvDataToList(self, "./Fitness2/Fitness-main/data/fitness_sessions_invalid.csv"))
        except FileNotFoundError:
            print("File not found.")
        #now lets remove error rows
        self.rows = rowValidator(self, self.rows)
            


        #now we have all rows in a list, lets give every participant their own rows
        assign_rows_to_participants(self, self.rows, participants)

        #We first get the data from the fitness tracker
        i = 0
        for participant in self.participants:
            participant.createSessions()

            # Now we need to handle the data
            for session in participant.sessions:
                if(len(session.observations) == 0): continue
                dataHandler = DataHandler(participant, session, self.badRecords)
                sessionClassifyer = SessionClassifyer(dataHandler) 
                # Generate report
                i += 1
                sessionClassifyer = SessionClassifyer(dataHandler)
                generateValidReport: ReportInterface = GenerateValidReport(dataHandler, sessionClassifyer, i)
                generateSummaryReport: GenerateSummaryReport = GenerateSummaryReport(participant,session,dataHandler,sessionClassifyer)
        #create the report with the errors
        generateErrorReport: ReportInterface = GenerateErrorReport(self.badRecords)
