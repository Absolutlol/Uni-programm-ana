
"""
Program: latvijas_nodokli.py
Latvijas nodokļu aprēķins 2026. gadam.

Aprēķina darbinieka algu pēc nodokļu nomaksas.
"""

# Initialize the constants
VSAOI_RATE = 0.105
TAX_RATE = 0.255
NON_TAXABLE_MINIMUM = 550.0
DEPENDENT_DEDUCTION = 250.0

# Request the inputs
grossIncome = float(input("Ievadi bruto algu (EUR): "))
numDependents = int(input("Ievadi apgādājamo skaitu: "))

# Calculate social insurance contributions
socialTax = grossIncome * VSAOI_RATE

# Calculate taxable income
taxableIncome = (grossIncome - socialTax
                 - NON_TAXABLE_MINIMUM
                 - DEPENDENT_DEDUCTION * numDependents)

# Taxable income cannot be negative
taxableIncome = max(0, taxableIncome)

# Calculate personal income tax
incomeTax = taxableIncome * TAX_RATE

# Calculate net salary
netIncome = grossIncome - socialTax - incomeTax

# Display the results
print("\n--- ALGAS APRĒĶINS ---")
print("Bruto alga:", round(grossIncome, 2), "EUR")
print("VSAOI (10.5%):", round(socialTax, 2), "EUR")
print("IIN (25.5%):", round(incomeTax, 2), "EUR")
print("Apgādājamo skaits:", numDependents)
print("Alga uz rokas:", round(netIncome, 2), "EUR")

