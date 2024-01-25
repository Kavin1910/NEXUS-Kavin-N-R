import tkinter as tk
from tkinter import ttk
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is the admission process for (\w+)?",
        ["The admission process for %1 usually includes a personal statement, high school transcript, SAT or ACT scores, and recommendation letters. Please visit the official college website for more details."]
    ],
    [
        r"how much does (\w+) cost?",
        ["%1 tuition fee is $%2. However, please note that this fee does not include housing, meal plans, or any additional expenses."]
    ],
    [
        r"what are the course requirements for (\w+)?",
        ["%1 is a course that requires strong foundation in %2 and %3. You will also need a good grasp of %4."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! We hope to see you again soon!"]
    ],
    [
        r".*",
        ["I'm not sure about that. Can you please provide more details?"]
    ]
]

reflections = {
    "i am" : "you are",
    "i was" : "you were",
    "i" : "you",
    "i'm" : "you're",
    "i'd" : "you'd",
    "i've" : "you've",
    "i'll" : "you'll",
    "my" : "your",
    "you are" : "I am",
    "you were" : "I was",
    "you've" : "I've",
    "you'll" : "I'll",
    "your" : "my",
    "yours" : "mine",
    "you" : "me",
    "me" : "you"
}

class ChatApp:
    def __init__(self, window):
        self.window = window
        self.window.title("College Admission Chatbot")
        self.chat_label = ttk.Label(self.window, text="")
        self.chat_label.pack(padx=20, pady=20, fill="both", expand=True)
        self.input_entry = ttk.Entry(self.window)
        self.input_entry.pack(fill="x", expand=True)
        self.input_entry.bind("<Return>", self.submit)
        self.chat_session = Chat(pairs, reflections)

    def submit(self, event):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, "end")
        self.chat_label['text'] = self.chat_session.respond(user_input)

root = tk.Tk()
chatbot = ChatApp(root)
root.mainloop()
