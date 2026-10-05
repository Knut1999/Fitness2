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
            flags["activity_level"] = "Activity level must be between 0 and 1"
        if float(observation["signal_quality"]) < 0 or float(observation["signal_quality"]) > 1:
            flags["signal_quality"] = "Signal quality must be between 0 and 1"
        if float(observation["skin_response"]) < 0 or float(observation["skin_response"]) > 100:
            flags["skin_response"] = "Skin response out of range"
        if float(observation["temperature"]) < 20 or float(observation["temperature"]) > 60:
            flags["temperature"] = "Temperature out of range"
        if float(observation["signal_quality"]) < 0 or float(observation["signal_quality"]) > 1:
            flags["signal_quality"] = "Poor signal quality"
        return flags