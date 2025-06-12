    from utils.fhir_loader import load_fhir_resource
🔍 Purpose: Imports the function that loads a FHIR-formatted JSON file from the utils/ folder.

    from rules.high_bp_rule import evaluate_bp
🔍 Purpose: Imports the blood pressure rule logic from the rules/ folder.

def main():
🚪 Purpose: Defines the entry point of the program — this is where the logic starts.

    observation = load_fhir_resource("fhir_samples/patient_1.json")
📥 Purpose: Loads a patient's clinical observation (e.g., blood pressure) from a FHIR JSON file.

    result = evaluate_bp(observation)
🧠 Purpose: Passes the FHIR observation into the blood pressure rule function.

Returns a CDS suggestion if BP > 140, otherwise returns None.

    if result:
        print("📋 CDS Suggestion Card")
        print(f"Summary: {result['summary']}")
        print(f"Detail: {result['detail']}")
        print(f"Indicator: {result['indicator']}")
📋 Purpose: If the rule is triggered, print a formatted suggestion card for the clinician to see.

    else:
        print("✅ No alerts. Patient is within normal range.")
✅ Purpose: If the rule is not triggered, indicate that everything is normal.

    if __name__ == "__main__":
    main()

🚦 Purpose: Ensures the main() function runs only when this script is executed directly, not when imported.

    💡 TL;DR Summary:
This script loads a sample patient observation (FHIR JSON), evaluates it against a blood pressure rule, and displays a CDS recommendation if the rule triggers.
