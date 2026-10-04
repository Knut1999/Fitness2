from abc import ABC, abstractmethod

class ReportInterface(ABC):

    @abstractmethod
    def writeToReport(self):
        pass