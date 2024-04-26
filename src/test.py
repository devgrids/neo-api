from ai.chat.gemini_chat import GeminiChat

chat = GeminiChat()

print(chat.send_message("Hola"))
print(chat.send_message("Puedes darme 10 vocabularios en ingles-spanish"))

print(chat.get_history())

