from ObservationValidator import ObservationValidator
from standaloneFunctions import calculate_summary


print("test for some important functions")


def calculate_summaryTest():
    print("Testing summary function")
    print(calculate_summary([1,2,3,4,5,6,7,8,9], 10))


def ObservationValidatorTest():
    print("First check static function with valid numbers")
    print(ObservationValidator.validate({
        "heart_rate": 65,
        "skin_response": 1.4,
        "activity_level": 0.12,
        "signal_quality": 0.13,
    }))

    print("Now check static function with non-valid numbers")
    print(ObservationValidator.validate({
        "heart_rate": 645,
        "skin_response": None,
        "activity_level": 4.12,
        "signal_quality": 10.13,
    }))


def boundaryTest():
    print("Testing boundary values")

    print(ObservationValidator.validate({
        "heart_rate": 20,
        "skin_response": 1.0,
        "activity_level": 0.5,
        "signal_quality": 0.5,
    }))

    print(ObservationValidator.validate({
        "heart_rate": 220,
        "skin_response": 1.0,
        "activity_level": 0.5,
        "signal_quality": 0.5,
    }))


def missingFileTest():
    print("Testing missing file")

    try:
        with open("file_that_does_not_exist.csv", "r") as file:
            file.read()
    except FileNotFoundError:
        print("File not found")


calculate_summaryTest()
ObservationValidatorTest()
boundaryTest()
missingFileTest()