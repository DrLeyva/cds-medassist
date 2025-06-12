def evaluate_glucose(observation):
    value = observation.get('valueQuantity', {}).get('value', 0)
    code = observation.get('code', {}).get('text', "").lower()

    if "glucose" in code and value > 200:
        return {
            "summary": "High Blood Glucose",
            "detail": f"Blood glucose level is {value} mg/dL. Recommend follow-up for diabetes screening.",
            "indicator": "warning"
        }

    return None
