#Standalone functions
import csv


def findParticipantData(Fitness, participants, csvFile):
    with open(csvFile, "r") as f:
        data = csv.DictReader(f)
        for row in data:
            print(row)


    
#values er liste med tall og i er 
def calculate_summary(values, i):
    if len(values) > 0:
        return {
            "Average": round(sum(values) / len(values),2),
            "Maximum": round(max(values), 2),
            "Minimum": round(min(values), 2),
            "Invalid measurements": i - len(values)
        }

    return {
        "Average": None,
        "Maximum": None,
        "Minimum": None,
        "Invalid measurements": i - len(values)
    }

#Innlevering 2
#Create participants
def participantDict():
    Participants = []
    with open("./fitness/Fitness-main/data/participants.csv", "r") as f:
        data = csv.reader(f)
        for row in data:
            if row[0] == "participant_id":
                continue
            participant = {}
            participant["id"] = row[0]
            participant["name"] = row[1]
            participant["baseline_heart_rate"] = row[2]
            participant["baseline_skin_response"] = row[3]
            participant["baseline_temperature"] = row[4]
            Participants.append(participant)

    return Participants
