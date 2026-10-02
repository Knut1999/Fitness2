class ObservationValidator:
    @staticmethod
    def validate(observation):
        flags = {}


        if observation["heart_rate"] is None:
            flags["heart_rate"] = "Missing heart rate"
        elif (int(observation["heart_rate"]) > 220 or int(observation["heart_rate"]) < 20):
            flags["heart_rate"] = "Too high/low"
        if observation["skin_response"] is None:
            flags["skin_response"] = "Missing skin response"
        if float(observation["activity_level"]) < 0 or float(observation["activity_level"]) > 1:
            flags["activity_level"] = "Signal quality must be between 0 and 1"
        if float(observation["signal_quality"]) < 0 or float(observation["signal_quality"]) > 1:
            flags["signal_quality"] = "Signal quality must be between 0 and 1"

        return flags