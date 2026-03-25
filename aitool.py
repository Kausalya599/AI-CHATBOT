import tkinter as tk

# Function to generate chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I'm your Python chatbot 😄"
    elif "how are you" in user_input:
        return "I'm doing great! What about you?"
    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence 🤖"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 👋"
    else:
        return "Sorry, I didn't understand that."

# Function to send message
def send_message():
    user_text = entry.get()
    chat_log.config(state=tk.NORMAL)
    
    chat_log.insert(tk.END, "You: " + user_text + "\n")
    
    response = get_response(user_text)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("Chatbot")

chat_log = tk.Text(window, state=tk.DISABLED, width=50, height=20)
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

window.mainloop()
