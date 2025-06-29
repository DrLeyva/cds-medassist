## 📄 fhir_loader.py — Detailed Walkthrough

```python
import json

def load_fhir_resource(path):
    with open(path, 'r') as file:
        return json.load(file)

🔍 Line-by-Line Breakdown
import json
📦 What it does:
Imports Python’s built-in json module.

🧠 Why it matters:
FHIR resources (like Observation, Patient, Medication, etc.) are commonly formatted as JSON.
This module is required to convert that JSON into Python dictionaries.

def load_fhir_resource(path):
🔧 What it does:
Defines a function named load_fhir_resource, which accepts a path (the file location of a .json file).

🔁 Why it’s useful:
You can reuse this function to load any FHIR-formatted file dynamically, such as:
load_fhir_resource("fhir_samples/patient_1.json")

with open(path, 'r') as file:
📂 What it does:
Opens the file located at path in read mode.

🧠 Why it's important:
Using with ensures the file is automatically closed after reading — this avoids memory or file locking issues, especially in production healthcare environments.

return json.load(file)
🔄 What it does:
Reads the file and parses the JSON into a native Python dictionary using json.load().

✅ Result:
You get a structured Python object that you can feed into your rule logic functions (like evaluate_bp()).

🧠 Real-World Analogy
Think of this like a nurse handing a clinician a structured chart:

You: "Load patient’s BP reading!"
This function: opens the digital chart, reads the data, and hands it over to your CDS logic in a format it understands.

✅ TL;DR Summary
The load_fhir_resource() function:

Opens a FHIR-formatted .json file

Converts it into a Python dictionary

Returns that dictionary for use in clinical decision logic

