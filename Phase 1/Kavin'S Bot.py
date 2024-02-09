import tkinter as tk
from tkinter import messagebox
import pyperclip

class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chatbot")
        self.geometry("400x500")
        self.text = tk.Text(self, wrap=tk.WORD)
        self.text.pack(expand=True, fill=tk.BOTH)

        self.text.tag_config("own", foreground="blue")
        self.text.tag_config("user", foreground="red")

        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.BOTTOM)

        self.input_field = tk.Entry(self.frame)
        self.input_field.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.send_button = tk.Button(self.frame, text="Send", command=self.send)
        self.send_button.pack(side=tk.RIGHT)

        self.questions = ["Whats your name?", "How old are you?", "What is your gender?", "Where do you live?", "What are your hobbies?"]
        self.send_message("Welcome to Kavin'S bot! I have some questions for you.")

    def send(self):
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.send_message(message)

        if message.lower() == "quit":
            self.send_message("Thank you Buddy! Have a Happy day!")
            self.destroy()

        elif len(self.questions) > 0:
            self.send_message(self.questions.pop(0))

    def send_message(self, message, tag="user"):
        self.text.insert(tk.END, str(message) + "\n", tag)
        self.text.see(tk.END)

def main():
    app = ChatApp()
    app.mainloop()

if __name__ == "__main__":
    main()
