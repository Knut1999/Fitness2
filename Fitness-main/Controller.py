from Fitness import Fitness
from standaloneFunctions import participantDict
from Participant import Participant
from pathlib import Path


class Controller: 
    #Konstruktør, her lager vi våres objekter
    def __init__(self,profiles,sessions,output):
        self.output = Path(output)
        self.blankReport()
        #get values we need from csv
        participantsDict = participantDict(profiles)
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
        self.fitness = Fitness(self.participants, sessions, self.output)

    def blankReport(self):
        self.output.mkdir(parents=True, exist_ok=True)

        with open(self.output / "analysis_report.txt", "w", encoding="utf-8") as file:
            file.write("")

        with open(self.output / "rejected_records.txt", "w", encoding="utf-8") as file:
            file.write("")

        with open(self.output / "analysis_summary.csv", "w", encoding="utf-8", newline="") as file:
            file.write("")

if __name__ == "__main__":
    controller = Controller()