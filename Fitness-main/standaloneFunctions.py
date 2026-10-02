#Standalone functions
import csv
import re

#regex
session_pattern = r"^FIT-\d{4}-\d{3}$"
participant_pattern = r"^P\d{3}$"
def findParticipantData(fitness, csvFile):
    with open(csvFile, "r") as f:
        data = csv.DictReader(f)

        
        for row in data:
            #check for error
            if not re.fullmatch(session_pattern, row["session_id"]):
                fitness.badRecords.append(row)
                continue
            if not re.fullmatch(participant_pattern, row["participant_id"]):
                fitness.badRecords.append(row)
                continue
            if(row["participant_id"] not in fitness.participants):
                fitness.badRecords.append(row)
                continue
            else:
                row_id = row["participant_id"]
                
                fitness.participants[row_id].observations.append(row)

    
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
