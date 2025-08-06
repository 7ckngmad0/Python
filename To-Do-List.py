import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.task_list = tk.Listbox(self.root, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.entry.get()
        self.tasks.append(task)
        self.task_list.insert(tk.END, task)
        self.entry.delete(0, tk.END)

    def remove_task(self):
        task_index = self.task_list.curselection()[0]
        self.tasks.pop(task_index)
        self.task_list.delete(task_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()