import google.generativeai as genai

# pip install google-generativeai
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")  # <-- YAHAN APNI KEY DAALO

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. You speak both Hindi and English. You are helpful, smart and respond concisely."
)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Jarvis: Goodbye!")
        break
    
    response = model.generate_content(user_input)
    print(f"Jarvis: {response.text}")