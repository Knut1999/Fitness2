from Fitness import Fitness
from standaloneFunctions import participantDict
from Participant import Participant2


class Controller: 
    #Konstruktør, her lager vi våres objekter
    def __init__(self):
        self.participants = [] #create participants
        participantsDict = participantDict()
        self.participants = []
        for participant in participantsDict:
            participant = Participant2(
                name=participant["name"],
                participant_id=participant["id"],
                baseline_heart_rate=participant["baseline_heart_rate"],
                baseline_skin_response=participant["baseline_skin_response"],
                baseline_temperature=participant["baseline_temperature"]
            )
            self.participants.append(participant)

        self.fitness = Fitness(self.participants)
        

if __name__ == "__main__":
    controller = Controller()