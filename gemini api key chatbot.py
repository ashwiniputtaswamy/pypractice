#pip install google-generativeai in your terminal
#code is below
import google.generativeai as genai

genai.configure(api_key="Your api key")

def chat_with_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

print("Hello, Iam a Chatbot! Ask anything!")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    reply = chat_with_gemini(prompt)
    print("Gemini: ",reply, "\n")
