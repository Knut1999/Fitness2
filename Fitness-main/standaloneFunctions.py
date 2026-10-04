from ObservationValidator import ObservationValidator
from Exceptions import InvalidSessionError, InvalidParticipantError
import csv
import re

#regex
session_pattern = r"^FIT-\d{4}-\d{3}$"
participant_pattern = r"^P\d{3}$"

def csvDataToList(fitness, csvFile):
    rows = []
    with open(csvFile, "r") as f:
        data = csv.DictReader(f)
        i = 0
        for row_number, row in enumerate(data, start=2):
            row["_filename"] = csvFile
            row["_row_number"] = row_number
            try:
                row["timestamp"] = int(row["timestamp"])
            except (ValueError, TypeError):
                fitness.badRecords.append([row, "timestamp", "Invalid numeric value"])
                continue

            try:
                row["heart_rate"] = int(row["heart_rate"])
            except (ValueError, TypeError):
                fitness.badRecords.append([row, "heart_rate", "Invalid numeric value"])
                continue

            try:
                row["skin_response"] = float(row["skin_response"])
            except (ValueError, TypeError):
                fitness.badRecords.append([row, "skin_response", "Invalid numeric value"])
                continue

            try:
                row["temperature"] = float(row["temperature"])
            except (ValueError, TypeError):
                fitness.badRecords.append([row, "temperature", "Invalid numeric value"])
                continue

            try:
                row["activity_level"] = float(row["activity_level"])
            except (ValueError, TypeError):
                fitness.badRecords.append([row, "activity_level", "Invalid numeric value"])
                continue

            try:
                row["signal_quality"] = float(row["signal_quality"])
            except (ValueError, TypeError):
                fitness.badRecords.append([row, "signal_quality", "Invalid numeric value"])
                continue
            rows.append(row)

    return rows

def assign_rows_to_participants(fitness, rows, participants):
    #use a dict with participant id: participant
    participantsDict = {}
    for participant in participants:
        participantsDict[participant.participant_id] = participant
    for row in rows:
        try:
            rowParticipantId = row["participant_id"]
            participantsDict[rowParticipantId].observations.append(row)
        except KeyError:
            fitness.badRecords.append([row, "participant_id", "Unknown participant ID"])


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

    try:
        with open("./Fitness2/Fitness-main/data/participants.csv", "r") as f:
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

    except FileNotFoundError:
        print("Participant file not found.")

    except PermissionError:
        print("Permission denied.")

    except csv.Error:
        print("CSV file error.")

    return Participants

def rowValidator(fitness, rows):
    rowsReturn = []
    for row in rows:
        flags = ObservationValidator.validate(row)
        if flags == {}:
            rowsReturn.append(row)
            continue
        else:
            fitness.badRecords.append([row, list(flags.keys())[0], list(flags.values())[0]])

    return rowsReturn
