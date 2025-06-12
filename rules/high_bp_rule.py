def evaluate_bp(observation):
    value = observation.get('valueQuantity', {}).get('value', 0)
    if value > 140:
        return {
            "summary": "High Blood Pressure",
            "detail": f"Systolic BP is {value} mmHg. Recommend lifestyle changes.",
            "indicator": "warning"
        }
    return None