from rules.glucose_rule import evaluate_glucose
from utils.fhir_loader import load_fhir_resource
from rules.high_bp_rule import evaluate_bp

def main():
    #observation = load_fhir_resource("fhir_samples/patient_1.json")
    observation = load_fhir_resource("fhir_samples/patient_glucose_2.json")
    bp_result = evaluate_bp(observation)
    glucose_result = evaluate_glucose(observation)

    if bp_result:
        print("📋 CDS Suggestion Card - Blood Pressure")
        print(f"Summary: {bp_result['summary']}")
        print(f"Detail: {bp_result['detail']}")
        print(f"Indicator: {bp_result['indicator']}")
        print("")

    if glucose_result:
        print("📋 CDS Suggestion Card - Glucose")
        print(f"Summary: {glucose_result['summary']}")
        print(f"Detail: {glucose_result['detail']}")
        print(f"Indicator: {glucose_result['indicator']}")
        print("")

    if not bp_result and not glucose_result:
        print("✅ No alerts. Patient is within normal range.")


if __name__ == "__main__":
    main()