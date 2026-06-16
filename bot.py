import pyautogui
import time
import pyperclip
import google.generativeai as genai

# pip install google-generativeai
genai.configure(api_key="AIzaSyB-rvc2zMXUkTvLslthvgrwfc0HE42vpv4")  

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""You are a person named Naruto who speaks hindi as well as english. 
You are from India and you are a coder. 
You analyze chat history and roast people in a funny way. 
Output should be the next chat response (text message only).
Do not start like this [21:02, 12/6/2024] Rohan Das: """
)

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False

# Step 1: Click on the chrome icon
pyautogui.click(1639, 1412)
time.sleep(1)

while True:
    time.sleep(5)
    # Step 2: Select text
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')
    # Step 3: Copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1994, 281)
    # Step 4: Get clipboard text
    chat_history = pyperclip.paste()
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        response = model.generate_content(chat_history)
        reply = response.text.strip()

        pyperclip.copy(reply)
        # Step 5: Click input box
        pyautogui.click(1808, 1328)
        time.sleep(1)
        # Step 6: Paste
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # Step 7: Send
        pyautogui.press('enter')