def get_response(user_input):
  user_input = user_input.lower()
  if "hello" in user_input:
    return "Hi"
  elif "how are you" in user_input:
    return "Iam awesome"
  else:
    return "I didn't understand"

def main():
  print("Welcome to rule based chatbot")
  print("type bye to exit")

  while True:
    user_input = input("You: ")
    if user_input.lower()=="bye":
      print("Goodbye")
      break
    else:
      response = get_response(user_input)
      print("Chatbot: ",response)
main()
