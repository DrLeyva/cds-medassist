# CDS-MedAssist

A simple mock Clinical Decision Support engine using FHIR-formatted data and Python logic.

## Features
- Loads FHIR Observation resources in JSON format
- Evaluates them against basic clinical logic (e.g., blood pressure thresholds)
- Outputs CDS-style recommendation cards

## Usage

```bash
python main.py
```

## Example Output

```
📋 CDS Suggestion Card
Summary: High Blood Pressure
Detail: Systolic BP is 150 mmHg. Recommend lifestyle changes.
Indicator: warning
```
---

Created by Aaron Leyva | Inspired by HL7 FHIR & CDS Hooks ecosystem
