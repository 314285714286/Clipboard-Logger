import pyperclip
import tkinter as tk
from tkinter import messagebox

class ClipboardLogger(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clipboard Logger")
        self.geometry("300x200")

        self.clipboard_history = []

        self.label = tk.Label(self, text="Clipboard History:")
        self.label.pack(pady=10)

        self.text = tk.Text(self, wrap=tk.WORD)
        self.text.pack(expand=True, fill=tk.BOTH)

        self.button = tk.Button(self, text="Clear History", command=self.clear_history)
        self.button.pack(pady=5)

        self.clipboard_check_interval = 1000  # Check clipboard every 1000 milliseconds (1 second)
        self.check_clipboard()

    def check_clipboard(self):
        current_clipboard_text = pyperclip.paste()

        if current_clipboard_text not in self.clipboard_history:
            self.clipboard_history.append(current_clipboard_text)
            self.text.delete(1.0, tk.END)

            for i, text in enumerate(self.clipboard_history):
                self.text.insert(tk.END, f"{i + 1}. {text}\n")

        self.after(self.clipboard_check_interval, self.check_clipboard)

    def clear_history(self):
        self.clipboard_history = []
        self.text.delete(1.0, tk.END)
        messagebox.showinfo("Clipboard Logger", "Clipboard history has been cleared.")

if __name__ == "__main__":
    app = ClipboardLogger()
    app.mainloop()