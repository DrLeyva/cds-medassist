# CDS-MedAssist 🩺💊  
*A Mock Clinical Decision Support (CDS) Engine built with Python + FHIR*

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FHIR](https://img.shields.io/badge/FHIR-HL7-red.svg)
![CDS](https://img.shields.io/badge/CDS-CQL%20Logic-lightgrey.svg)

---

## 🚀 Overview

**CDS-MedAssist** is a lightweight Clinical Decision Support engine that mimics real-world CDS behavior using:
- HL7 FHIR JSON resources (Observations)
- Custom Python rule logic inspired by CQL/CPG-on-FHIR
- Clear, interpretable decision cards (CDS Hooks–style)

This project was built to showcase knowledge of structured healthcare data, clinical logic, and Python-based decision support for EHR-like environments.

---

## 🧠 Example Use Case

When run against a FHIR `Observation` file containing a **systolic blood pressure** of `150 mmHg`, the engine returns:

📋 CDS Suggestion Card
Summary: High Blood Pressure
Detail: Systolic BP is 150 mmHg. Recommend lifestyle changes.
Indicator: warning
---


---

## 🧰 Tech Stack

- Python 3.10
- FHIR JSON resource parsing
- Custom CDS logic engine
- Modular Python (rule engine, loader, utils)

---

## 📁 Project Structure

<pre>
cds-medassist/
├── main.py                 # Entry point
├── fhir_samples/           # Sample FHIR Observation resources
├── rules/                  # Rule logic (e.g., BP threshold)
├── utils/                  # Helper functions (FHIR loader)
├── requirements.txt
├── README.md
└── .gitignore
</pre>

---

## 🛠️ Setup

Clone the repo and run:
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py


---

## 🧪 Sample Output

📋 CDS Suggestion Card
Summary: High Blood Pressure
Detail: Systolic BP is 150 mmHg. Recommend lifestyle changes.
Indicator: warning


---

## 📌 Next Steps

- [ ] Add glucose, cholesterol, and BMI rules
- [ ] Build Flask web interface for file uploads
- [ ] Accept real-time FHIR bundles via REST API
- [ ] Expand support for CDS Hooks format

---

## 👨‍⚕️ Created By

**Aaron Leyva**  
Master’s in Computer Science | Clinical Tech Enthusiast  
[GitHub](https://github.com/DrLeyva) • [LinkedIn](https://www.linkedin.com/in/aaron-leyva-sala-17a56a134/)

---

⭐ Star this repo if you want to see it grow!
