import tkinter as tk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Maker")
        
        self.flashcards = []
        
        self.question_label = tk.Label(root, text="Question:")
        self.question_label.pack()
        
        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.pack()
        
        self.answer_label = tk.Label(root, text="Answer:")
        self.answer_label.pack()
        
        self.answer_entry = tk.Entry(root, width=50)
        self.answer_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack()
        
        self.show_button = tk.Button(root, text="Show Flashcards", command=self.show_flashcards)
        self.show_button.pack()
        
    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if question and answer:
            self.flashcards.append((question, answer))
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Flashcard added!")
        else:
            messagebox.showwarning("Input Error", "Please enter both question and answer.")
    
    def show_flashcards(self):
        if not self.flashcards:
            messagebox.showinfo("No Flashcards", "No flashcards available.")
            return
        
        for question, answer in self.flashcards:
            messagebox.showinfo("Flashcard", f"Question: {question}\nAnswer: {answer}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()