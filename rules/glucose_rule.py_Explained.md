## 🧠 glucose_rule.py — Detailed Walkthrough

```python
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

🔍 Line-by-Line Breakdown
def evaluate_glucose(observation):
Defines a function that takes a single FHIR Observation object (dict format).

value = observation.get(...)
Safely retrieves the numeric glucose value; defaults to 0 if missing.

code = observation.get(...).lower()
Retrieves and lowercases the observation code/text (e.g., “Blood Glucose”) for reliable rule matching.

if "glucose" in code and value > 200:
Checks whether this is a glucose observation and if the value exceeds the threshold (200 mg/dL).

return { ... }
Returns a CDS suggestion dictionary if criteria are met (summary, detail, and indicator).

return None
Returns None when no rule conditions are satisfied, indicating no alert.

✅ TL;DR Summary:
This function reads a patient’s glucose reading and triggers a clinical recommendation if the level is over 200 mg/dL—mirroring real-world diabetes alert logic.
