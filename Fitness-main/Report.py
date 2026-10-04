from DataHandler import DataHandler
from SessionClassifyer import SessionClassifyer

from ReportInterface import ReportInterface

class GenerateValidReport(ReportInterface):
    def __init__(self, DataHandler: DataHandler, SessionClassifyer: SessionClassifyer, i):
        self.i = i
        self.dataHandler = DataHandler
        self.sessionClassifyer = SessionClassifyer
        self.participant = self.dataHandler.participant
        self.writeToReport()

    
    def writeToReport(self):
        
        result = (f"{'=' * 50} \n")
        result += (f"FITNESS SESSION REPORT {self.i}\n")
        result += (f"{'=' * 50}\n")
        result += (f"\n")
        result += (f"Name: {self.participant.name} \n")
        result += (f"Reference ID: {self.participant.profile['participant_id']}") + "\n"
        result += (f"Baseline heart rate: {self.participant.profile['baseline_heart_rate']} bpm") + "\n"
        result += (f"Baseline skin response: {self.participant.profile['baseline_skin_response']}") + "\n"
        result += (f"Baseline temperature: {self.participant.profile['baseline_temperature']}°C") + "\n"

        result += f"Number of measurements: {len(self.dataHandler.observations) + self.dataHandler.badRecordsInt}\n"
        result += f"Usable measurements: {len(self.dataHandler.observations)}\n"
        result += f"Invalid measurements: {self.dataHandler.badRecordsInt}\n"

        result += f"Session classification: {self.sessionClassifyer.classification}\n"
        result += f"Reason: {self.sessionClassifyer.reason}\n"
        result += "\n"

        result += (f"{'Heart rate summary':<24}|{'Skin response summary':<24}|{'Temperature summary':<24}|{'Activity level summary':<24}|{'Signal quality summary'}\n")
        result += (f"{'Average: ' + str(self.dataHandler.heart_rate_summary['Average']):<24}|{'Average: ' + str(self.dataHandler.skin_response_summary['Average']):<24}|{'Average: ' + str(self.dataHandler.temperature_summary['Average']):<24}|{'Average: ' + str(self.dataHandler.activity_level_summary['Average']):<24}|{'Average: ' + str(self.dataHandler.signal_quality_summary['Average'])}\n")
        result += (f"{'Maximum: ' + str(self.dataHandler.heart_rate_summary['Maximum']):<24}|{'Maximum: ' + str(self.dataHandler.skin_response_summary['Maximum']):<24}|{'Maximum: ' + str(self.dataHandler.temperature_summary['Maximum']):<24}|{'Maximum: ' + str(self.dataHandler.activity_level_summary['Maximum']):<24}|{'Maximum: ' + str(self.dataHandler.signal_quality_summary['Maximum'])}\n")
        result += (f"{'Minimum: ' + str(self.dataHandler.heart_rate_summary['Minimum']):<24}|{'Minimum: ' + str(self.dataHandler.skin_response_summary['Minimum']):<24}|{'Minimum: ' + str(self.dataHandler.temperature_summary['Minimum']):<24}|{'Minimum: ' + str(self.dataHandler.activity_level_summary['Minimum']):<24}|{'Minimum: ' + str(self.dataHandler.signal_quality_summary['Minimum'])}\n")
        result += (f"{'Invalid measurements: ' + str(self.dataHandler.heart_rate_summary['Invalid measurements']):<24}|{'Invalid measurements: ' + str(self.dataHandler.skin_response_summary['Invalid measurements']):<24}|{'Invalid measurements: ' + str(self.dataHandler.temperature_summary['Invalid measurements']):<24}|{'Invalid measurements: ' + str(self.dataHandler.activity_level_summary['Invalid measurements']):<24}|{'Invalid measurements: ' + str(self.dataHandler.signal_quality_summary['Invalid measurements'])}\n")        
                
        result += (f"\n")
        result += (f"{'=' * 50}\n")
        result += (f"RECOVERY \n")
        result += (f"{'=' * 50} \n")
        if(self.dataHandler.heart_rate_summaryBeginning["Invalid measurements"] != 0 or self.dataHandler.heart_rate_summaryEnd["Invalid measurements"] != 0):
            result += f"Cannot check the recovery because of invalid measurements in the beginning/end \n"
        else:
            result += f"Heart rate average in the first half: {self.dataHandler.heart_rate_summaryBeginning["Average"]} \n"
            result += f"Heart rate average in the last half: {self.dataHandler.heart_rate_summaryEnd["Average"]} \n"
            if(self.dataHandler.heart_rate_summaryBeginning["Average"] > self.dataHandler.heart_rate_summaryEnd["Average"]):
                result += "Heart rate did recover well near the end \n"
            else:
                result += "Heart rate did not recover well near the end \n"

        if(self.dataHandler.activity_level_summaryBeginning["Invalid measurements"] != 0 or self.dataHandler.activity_level_summaryEnd["Invalid measurements"] != 0):
            result += f"Cannot check the recovery because of invalid measurements in the beginning/end \n"
        else:
            result += f"Activity level average in the first half: {self.dataHandler.activity_level_summaryBeginning["Average"]} \n"
            result += f"Activity level average in the last half: {self.dataHandler.activity_level_summaryEnd["Average"]} \n"
            if(self.dataHandler.activity_level_summaryBeginning["Average"] > self.dataHandler.activity_level_summaryEnd["Average"]):
                result += "Activity level did recover well near the end \n"
            else:
                result += "Activity level did not recover well near the end \n"

        with open("Fitness2/Fitness-main/output/analysis_report.txt", "a", encoding="utf-8") as file:
            file.write(result)


class GenerateErrorReport(ReportInterface):
    def __init__(self, badRecords):
        self.badRecords = badRecords
        self.writeToReport()

    def writeToReport(self):
        
        result = (f"{'=' * 50} \n")
        result += (f"FITNESS SESSION ERRORS \n")
        result += (f"{'=' * 50}\n")
        result += (f"\n")
        for error in self.badRecords:
            row = error[0]
            result += f"File: {row['_filename']} \n"
            result += f"Row: {row['_row_number']} \n"
            result += f"Field: {error[1]} \n"
            result += f"The error is: {error[2]} \n"
            result += f"The line is: {row}\n"
            result += "\n"

        with open("Fitness2/Fitness-main/output/rejected_records.txt", "a", encoding="utf-8") as file:
            file.write(result)

import csv
class GenerateSummaryReport(ReportInterface):
    def __init__(self, participant, session, dataHandler, sessionClassifyer):
        self.participant = participant
        self.session = session
        self.dataHandler = dataHandler
        self.sessionClassifyer = sessionClassifyer
        self.writeToReport()

    def writeToReport(self):
        with open(
            "Fitness2/Fitness-main/output/analysis_summary.csv",
            "a",
            encoding="utf-8",
            newline=""
        ) as file:

            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow([
                    "participant_id",
                    "session_id",
                    "classification",
                    "reason",
                    "average_heart_rate",
                    "average_skin_response",
                    "average_temperature",
                    "average_activity_level",
                    "average_signal_quality",
                    "usable_measurements",
                    "invalid_measurements"
                ])

            writer.writerow([
                self.participant.participant_id,
                self.session.sessionID,
                self.sessionClassifyer.classification,
                self.sessionClassifyer.reason,
                self.dataHandler.heart_rate_summary["Average"],
                self.dataHandler.skin_response_summary["Average"],
                self.dataHandler.temperature_summary["Average"],
                self.dataHandler.activity_level_summary["Average"],
                self.dataHandler.signal_quality_summary["Average"],
                len(self.dataHandler.observations),
                self.dataHandler.badRecordsInt
            ])