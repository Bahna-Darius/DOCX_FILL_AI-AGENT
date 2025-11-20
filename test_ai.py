from config import API_KEY, MODEL_NAME
import google.generativeai as genai


genai.configure(api_key=API_KEY)


def test_stable_connection():
    print("Testing connection with a STABLE model...")

    try:
        model = genai.GenerativeModel(MODEL_NAME)

        response = model.generate_content("Hello! Are you ready to help me fill out some forms?")

        print("\n--- AI RESPONSE ---")
        print(response.text)
        print("\nSUCCESS!")

    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")


if __name__ == "__main__":
    test_stable_connection()
