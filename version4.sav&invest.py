import tkinter as tk
from tkinter import ttk
import locale

# Set the locale to format currency
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

class Investment:
    def __init__(self, max_investment_per_year, min_monthly_investment, min_initial_investment, predicted_returns, estimated_tax, fees_rate):
        self.max_investment_per_year = max_investment_per_year
        self.min_monthly_investment = min_monthly_investment
        self.min_initial_investment = min_initial_investment
        self.predicted_returns = predicted_returns
        self.estimated_tax = estimated_tax
        self.fees_rate = fees_rate

def calculate_returns(investment, initial_sum, monthly_investment, years):
    total_returns = 0
    total_fees = 0
    total_taxes = 0

    for year in range(1, years + 1):
        # Calculate returns and fees for each year
        returns = (initial_sum + (monthly_investment * 12 * year)) * (investment.predicted_returns[1] / 100)
        fees = (initial_sum + (monthly_investment * 12 * year)) * (investment.fees_rate / 100)
        
        # Calculate taxes based on estimated tax rates
        taxable_profit = max(0, returns - initial_sum - (monthly_investment * 12 * year))
        tax = 0
        for tax_threshold, tax_rate in investment.estimated_tax.items():
            if taxable_profit > tax_threshold:
                tax += (taxable_profit - tax_threshold) * (tax_rate / 100)

        total_returns += returns
        total_fees += fees
        total_taxes += tax

    return total_returns, total_fees, total_taxes

def display_quote(investment, returns, fees, taxes, years):
    result_label.config(text=f"\nInvestment Quote:\n\n{years} Year(s):\n"
                             f"Returns: {locale.currency(returns, grouping=True)}\n"
                             f"Fees: {locale.currency(fees, grouping=True)}\n"
                             f"Taxes: {locale.currency(taxes, grouping=True)}")

def calculate_quote():
    try:
        investment_choice = investment_combobox.current() + 1
        initial_sum = float(initial_sum_entry.get())
        monthly_investment = float(monthly_investment_entry.get())
        investment_duration = int(years_combobox.get())

        options = {
            1: Investment(20000, 50, None, (1.2, 2.4), {0: 0}, 0.25),
            2: Investment(30000, 50, 300, (3, 5.5), {12000: 10}, 0.3),
            3: Investment(float('inf'), 150, 1000, (4, 23), {12000: 10, 40000: 20}, 1.3),
        }

        if investment_choice not in options:
            result_label.config(text="Invalid investment option. Please choose 1, 2, or 3.")
            return

        selected_investment = options[investment_choice]

        if investment_duration not in [1, 5, 10]:
            result_label.config(text="Invalid investment duration. Please choose 1, 5, or 10 years.")
            return

 
        if selected_investment.min_initial_investment is not None and initial_sum < selected_investment.min_initial_investment:
            result_label.config(text=f"Initial sum must be at least {locale.currency(selected_investment.min_initial_investment, grouping=True)}.")
            return


        if monthly_investment < selected_investment.min_monthly_investment:
            result_label.config(text=f"Monthly investment must be at least {locale.currency(selected_investment.min_monthly_investment, grouping=True)}.")
            return

        if (initial_sum + (monthly_investment * 12 * investment_duration)) > selected_investment.max_investment_per_year * investment_duration:
            result_label.config(text=f"The total investment exceeds the maximum allowed per year "
                                     f"({locale.currency(selected_investment.max_investment_per_year, grouping=True)} per year).")
            return

        returns, fees, taxes = calculate_returns(selected_investment, initial_sum, monthly_investment, investment_duration)
        display_quote(selected_investment, returns, fees, taxes, investment_duration)

    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numerical values.")

# GUI
root = tk.Tk()
root.title("Savings and Investments Module")

# Investment options
investment_options = {
    1: "Basic Savings Plan",
    2: "Savings Plan Plus",
    3: "Managed Stock Investments",
}

# Labels and Entry Widgets
investment_label = tk.Label(root, text="Select Investment:")
investment_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

investment_combobox = ttk.Combobox(root, values=list(investment_options.values()), state="readonly")
investment_combobox.current(0)
investment_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

initial_sum_label = tk.Label(root, text="Initial Lump Sum (GBP):")
initial_sum_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

initial_sum_entry = tk.Entry(root)
initial_sum_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

monthly_investment_label = tk.Label(root, text="Monthly Investment (GBP):")
monthly_investment_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

monthly_investment_entry = tk.Entry(root)
monthly_investment_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

years_label = tk.Label(root, text="Investment Duration (Years):")
years_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

years_combobox = ttk.Combobox(root, values=[1, 5, 10], state="readonly")
years_combobox.current(0)
years_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Button to calculate quote
calculate_button = tk.Button(root, text="Calculate Quote", command=calculate_quote)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Display result
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
