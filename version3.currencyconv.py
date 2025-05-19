import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

exchange_rates = {
    'GBP': 1.0,
    'USD': 1.33,
    'EUR': 1.18,
    'BRL': 7.16,
    'JPY': 148.50,
    'TKY': 149.50,
}

def calculate_fee(amount):
    if amount <= 500:
        return 0.035  # 3.5%
    elif amount <= 1500:
        return 0.027  # 2.7%
    elif amount <= 2500:
        return 0.02   # 2.0%
    else:
        return 0.015  # 1.5%

def plot_transaction_graph(transactions):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(transactions, marker='o', linestyle='-')
    ax.set_xlabel('Transaction Number')
    ax.set_ylabel('Converted Amount')
    ax.set_title('Transaction History')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

def save_graph():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            plt.savefig(file_path)
            messagebox.showinfo("Save Graph", "Graph saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred while saving the graph: {str(e)}")

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()

        if amount < 300:
            result.set("Minimum transaction amount is 300.")
            return
        elif amount > 5000:
            result.set("Maximum transaction amount is 5000.")
            return

        if from_currency == to_currency:
            result.set("Cannot convert between the same currencies.")
        else:
            converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
            
            fee_percentage = calculate_fee(amount)
            fees = converted_amount * fee_percentage
            
            converted_amount_with_fees = converted_amount - fees
            
            result.set(f"{amount:.2f} {from_currency} = {converted_amount_with_fees:.2f} {to_currency} (fees: {fees:.2f} {to_currency})")

            transactions.append(converted_amount_with_fees)
            plot_transaction_graph(transactions)

    except ValueError:
        result.set("Invalid input. Please enter a valid number.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

window = tk.Tk()
window.title("Currency Converter")

label_amount = tk.Label(window, text="Amount:")
label_amount.grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_from_currency = tk.Label(window, text="From Currency:")
label_from_currency.grid(row=1, column=0, padx=10, pady=10)
combo_from_currency = tk.StringVar()
combo_from_currency.set('GBP')
dropdown_from_currency = tk.OptionMenu(window, combo_from_currency, *exchange_rates.keys())
dropdown_from_currency.grid(row=1, column=1, padx=10, pady=10)

label_to_currency = tk.Label(window, text="To Currency:")
label_to_currency.grid(row=2, column=0, padx=10, pady=10)
combo_to_currency = tk.StringVar()
combo_to_currency.set('USD')
dropdown_to_currency = tk.OptionMenu(window, combo_to_currency, *exchange_rates.keys())
dropdown_to_currency.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, pady=10)

save_button = tk.Button(window, text="Save Graph", command=save_graph)
save_button.grid(row=3, column=1, pady=10)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

transactions = []

window.mainloop()
