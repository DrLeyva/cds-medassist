from utils.fhir_loader import load_fhir_resource
from rules.high_bp_rule import evaluate_bp

def main():
    observation = load_fhir_resource("fhir_samples/patient_1.json")
    result = evaluate_bp(observation)
    if result:
        print("📋 CDS Suggestion Card")
        print(f"Summary: {result['summary']}")
        print(f"Detail: {result['detail']}")
        print(f"Indicator: {result['indicator']}")
    else:
        print("✅ No alerts. Patient is within normal range.")

if __name__ == "__main__":
    main()