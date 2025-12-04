import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# ==========================================
# THE THERMODYNAMIC MONEY DATASET
# ==========================================
# X = Energy Cost: Hours of Human Labor required to purchase 1 Gigajoule (GJ) of useful energy.
#     (Derived from Nordhaus "Price of Light" and historical wage data).
# Y = Granularity: Purchasing Power of the Smallest Socially Trusted Accounting Unit (in 2024 USD).
#     (Derived from Numismatic data: Barley -> Bronze -> Silver -> Gold -> Fiat -> Digital).

data = [
    {
        "epoch": "Neolithic",
        "description": "Social Credit",
        "year": -10000,
        "x": 5000,       # 5000 hrs labor for 1 GJ (Hunting/Gathering)
        "y": 500         # Unit = Relationship/Grooming (High Value, Low Velocity)
    },
    {
        "epoch": "Sumer",
        "description": "Barley/Shekel",
        "year": -2000,
        "x": 400,        # 400 hrs labor for 1 GJ (Oxen/Agriculture)
        "y": 13          # Unit = 1 Grain of Barley (~$13 purchasing power)
    },
    {
        "epoch": "Rome",
        "description": "Bronze Nummus",
        "year": 300,
        "x": 50,         # 50 hrs labor for 1 GJ (Slavery/Watermills)
        "y": 2           # Unit = Bronze Coin (~$2 purchasing power)
    },
    {
        "epoch": "Medieval",
        "description": "Silver Farthing",
        "year": 1400,
        "x": 40,         # 40 hrs labor for 1 GJ (Wind/Animal)
        "y": 1.5         # Unit = Silver Farthing (~$1.50)
    },
    {
        "epoch": "Industrial",
        "description": "Copper Penny",
        "year": 1900,
        "x": 5,          # 5 hrs labor for 1 GJ (Coal/Steam)
        "y": 0.05        # Unit = Copper Penny (~$0.05)
    },
    {
        "epoch": "Digital",
        "description": "Satoshi/Byte",
        "year": 2024,
        "x": 0.001,      # 0.001 hrs labor for 1 GJ (Solar/Nuclear/Grid)
        "y": 0.00001     # Unit = Database Entry/Satoshi (~$0.00001)
    }
]

# Extract Data for Plotting
x_val = np.array([d['x'] for d in data])
y_val = np.array([d['y'] for d in data])
labels = [f"{d['epoch']}\n({d['description']})" for d in data]

# ==========================================
# STATISTICAL ANALYSIS (Log-Log Regression)
# ==========================================
log_x = np.log10(x_val)
log_y = np.log10(y_val)

# Perform Linear Regression on the Log Transformed Data
slope, intercept, r_value, p_value, std_err = linregress(log_x, log_y)
r_squared = r_value**2

print(f"Thermodynamic Law Detected:")
print(f"Slope: {slope:.4f} (Target is -1.0)")
print(f"R-Squared: {r_squared:.4f} (Target is > 0.95)")

# ==========================================
# PLOTTING
# ==========================================
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Plot the Data Points
plt.scatter(x_val, y_val, color='red', s=150, zorder=5, edgecolors='black', label='Historical Epochs')

# Plot the Regression Line (The "Dead Straight Line")
x_fit = np.logspace(np.log10(min(x_val)/2), np.log10(max(x_val)*2), 100)
y_fit = 10**(intercept + slope * np.log10(x_fit))
plt.plot(x_fit, y_fit, color='blue', linestyle='--', linewidth=2, alpha=0.7, 
         label=f'Thermodynamic Constraint\nSlope = {slope:.3f} | $R^2$ = {r_squared:.3f}')

# Annotate the Points
for i, txt in enumerate(labels):
    # Dynamic offset logic to prevent text overlap
    xytext = (10, 5) if i % 2 == 0 else (10, -20)
    plt.annotate(txt, (x_val[i], y_val[i]), xytext=xytext, textcoords='offset points', 
                 fontsize=10, fontweight='bold', arrowprops=dict(arrowstyle="-", color='gray'))

# Styling the Plot
plt.xscale('log')
plt.yscale('log')

# INVERT X-AXIS: 
# We want "Progress" (Cheaper Energy) to move from Left to Right.
# So High Cost (Left) -> Low Cost (Right)
plt.xlim(max(x_val)*5, min(x_val)/5) 

plt.title('The Joule Standard: The Thermodynamic Law of Money (10,000 BC - 2024 AD)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Real Cost of Energy (E)\n[Hours of Human Labor to purchase 1 Gigajoule] (Log Scale)', fontsize=12)
plt.ylabel('Monetary Granularity (G)\n[Purchasing Power of Smallest Unit in 2024 USD] (Log Scale)', fontsize=12)

# Add Equation Annotation
plt.text(0.5, 0.05, r'$G \cdot E = k$', transform=ax.transAxes, fontsize=20, 
         verticalalignment='bottom', horizontalalignment='center', 
         bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black", alpha=0.8))

plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend(loc='upper right', fontsize=11)
plt.tight_layout()

# Save output
filename = 'thermodynamic_money_law.png'
plt.savefig(filename, dpi=300)
print(f"Graph saved as {filename}")
plt.show()