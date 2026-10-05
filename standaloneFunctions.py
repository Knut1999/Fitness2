from ObservationValidator import ObservationValidator
from Exceptions import InvalidRowError, InvalidParticipantError
import csv
import re

#regex
session_pattern = r"^FIT-\d{4}-\d{3}$"
participant_pattern = r"^P\d{3}$"

def csvDataToList(fitness, csvFile):
    rows = []
    with open(csvFile, "r", encoding="utf-8", newline="") as f:
        data = csv.DictReader(f)
        i = 0

        required_fields = ["session_id","participant_id","timestamp","heart_rate","skin_response","temperature","activity_level","signal_quality"]
        for row_number, row in enumerate(data, start=2):
            row["_filename"] = csvFile
            row["_row_number"] = row_number
            #regex and key error handling
            try:
                if not re.fullmatch(session_pattern, row["session_id"]):
                    fitness.badRecords.append([row, "session_id", "Invalid identifier(regex)"])
                    continue

                if not re.fullmatch(participant_pattern, row["participant_id"]):
                    fitness.badRecords.append([row, "participant_id", "Invalid identifier(regex)"])
                    continue

            except KeyError as e:
                fitness.badRecords.append([row, str(e), "Missing required field"])
                continue
            if len(row) != 10:
                fitness.badRecords.append(
                    [row, "row", "Unexpected row length"]
                )
                continue
            if any(field not in row or row[field] == "" for field in required_fields):
                fitness.badRecords.append([row, "required_field", "Missing required field"])
                continue

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
            if row["participant_id"] not in participantsDict:
                raise InvalidParticipantError("Unknown participant")
        except InvalidParticipantError:
            fitness.badRecords.append(
                [row, "participant_id", "Unknown participant"]
            )
            continue
        try:
            if row["session_id"] == "":
                raise InvalidRowError("Invalid session")
        except InvalidRowError:
            fitness.badRecords.append(
                [row, "session_id", "Invalid session"]
            )
            continue
        participant = participantsDict[row["participant_id"]]
        participant.observations.append(row)

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
def participantDict(input):
    Participants = []

    try:
        with open(input, "r") as f:
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
