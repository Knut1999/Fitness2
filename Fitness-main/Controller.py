from Fitness import Fitness
from standaloneFunctions import participantDict
from Participant import Participant2


class Controller: 
    #Konstruktør, her lager vi våres objekter
    def __init__(self):
        #get values we need from csv
        participantsDict = participantDict()
        #make a dict for later, it will have -> {id, participant}
        self.participants = {}

        for participantValues in participantsDict:
            #make participants
            participant = Participant2(
                name=participantValues["name"],
                participant_id=participantValues["id"],
                baseline_heart_rate=participantValues["baseline_heart_rate"],
                baseline_skin_response=participantValues["baseline_skin_response"],
                baseline_temperature=participantValues["baseline_temperature"]
            )
            id = participantValues["id"]
            self.participants[id] = participant
     
        #we create the fitness class
        self.fitness = Fitness(self.participants)
        

if __name__ == "__main__":
    controller = Controller()