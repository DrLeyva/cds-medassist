## 🧾 patient_1.json — What Is This?

This file contains a sample **FHIR `Observation`** resource representing a patient's **systolic blood pressure reading**.

In real-world clinical systems (e.g., Epic, Cerner), patient data is often structured in this format and exchanged through secure APIs.

Example snippet:

```json
{
  "resourceType": "Observation",
  "id": "bp-reading-1",
  "valueQuantity": {
    "value": 150,
    "unit": "mmHg"
  },
  "status": "final",
  "code": {
    "text": "Blood Pressure"
  },
  "subject": {
    "reference": "Patient/1"
  }
}
