import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spell Checker")
        self.spell = SpellChecker()

        # Setting up the UI elements
        self.text_input_label = tk.Label(root, text="Enter text:")
        self.text_input_label.pack(pady=10)

        self.text_input = tk.Text(root, height=10, width=40)
        self.text_input.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack(pady=10)

        self.corrected_text_label = tk.Label(root, text="Corrected text will appear here:")
        self.corrected_text_label.pack(pady=10)

        self.corrected_text_output = tk.Label(root, text="", wraplength=400)
        self.corrected_text_output.pack(pady=10)

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            corrected_words.append(corrected_word)

        return " ".join(corrected_words)

    def check_spelling(self):
        input_text = self.text_input.get("1.0", tk.END).strip()

        if not input_text:
            messagebox.showwarning("Input Error", "Please enter some text to check.")
            return

        corrected_text = self.correct_text(input_text)
        self.corrected_text_output.config(text=corrected_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
