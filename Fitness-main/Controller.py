from Fitness import Fitness
from standaloneFunctions import participantDict
from Participant import Participant


class Controller: 
    #Konstruktør, her lager vi våres objekter
    def __init__(self):
        self.blankReport()
        #get values we need from csv
        participantsDict = participantDict()
        #make a dict for later, it will have -> {id, participant}
        self.participants = []

        for participantValues in participantsDict:
            #make participants
            participant = Participant(
                name=participantValues["name"],
                participant_id=participantValues["id"],
                baseline_heart_rate=participantValues["baseline_heart_rate"],
                baseline_skin_response=participantValues["baseline_skin_response"],
                baseline_temperature=participantValues["baseline_temperature"]
            )
            self.participants.append(participant)
     
        #we create the fitness class
        self.fitness = Fitness(self.participants)

    def blankReport(self):
        with open("Fitness2/Fitness-main/output/analysis_report.txt", "w", encoding="utf-8") as file:
            file.write("")

        with open("Fitness2/Fitness-main/output/rejected_records.txt", "w", encoding="utf-8") as file:
            file.write("")

        with open("Fitness2/Fitness-main/output/analysis_summary.csv", "w", encoding="utf-8", newline="") as file:
            file.write("")

if __name__ == "__main__":
    controller = Controller()