import tkinter as tk
from tkinter import messagebox

# Define the ExpenseTrackerApp class
class ExpenseTrackerApp:
    def __init__(self, root):  # The __init__ method should accept 'root' as a parameter
        self.root = root  # Store the root window reference
        self.root.title("Expense Tracker")  # Set the window title
        self.root.geometry("400x300")  # Set the window size

        # Setting up the main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Label for title
        self.title_label = tk.Label(self.frame, text="Expense Tracker", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Entry for expense name
        self.name_label = tk.Label(self.frame, text="Expense Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack(pady=5)

        # Entry for expense amount
        self.amount_label = tk.Label(self.frame, text="Expense Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.frame)
        self.amount_entry.pack(pady=5)

        # Button to add expense
        self.add_button = tk.Button(self.frame, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=10)

        # Listbox to display expenses
        self.expense_listbox = tk.Listbox(self.frame)
        self.expense_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_expense(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()

        if not name or not amount:
            messagebox.showwarning("Input Error", "Please enter both name and amount")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the amount")
            return

        expense = f"{name}: ${amount:.2f}"
        self.expense_listbox.insert(tk.END, expense)

        # Clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

# Main application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = ExpenseTrackerApp(root)  # Instantiate the app with the root window
    root.mainloop()  # Start the Tkinter event loop
