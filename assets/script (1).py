# Create economic analysis for HomeBridge
import numpy as np

# Market sizing data
market_data = {
    'Market Segment': [
        'UK Family Carers (5.8M)', 'UK Adults 65+ (12M)', 'UK Elderly Living Alone (3.5M)',
        'Voice AI Healthcare Market', 'Computer Vision Healthcare Market', 'Digital Health Market UK'
    ],
    'Target Addressable Market': [
        '1.2M families (willing to pay)', '800K elderly (tech-ready)', '400K high-need elderly',
        '$2.1B global by 2027', '$3.8B global by 2027', '£8.2B UK by 2025'
    ],
    'ARPU Potential (Annual)': [
        '£300-600', '£180-400', '£400-800',
        'N/A', 'N/A', 'N/A'
    ],
    'Market Maturity': [
        'Early Stage', 'Growing', 'Underserved',
        'Growth Stage', 'Early Stage', 'Mature'
    ]
}

# Create revenue model scenarios
years = np.array([2025, 2026, 2027, 2028, 2029])
conservative_users = np.array([500, 2500, 8000, 20000, 35000])
optimistic_users = np.array([1000, 5000, 15000, 40000, 70000])
arpu = np.array([300, 350, 400, 450, 500])  # Annual Revenue Per User

conservative_revenue = conservative_users * arpu / 1000  # in thousands
optimistic_revenue = optimistic_users * arpu / 1000

print("=== HOMEBRIDGE REVENUE PROJECTIONS ===")
print(f"{'Year':<6} {'Conservative Users':<18} {'Optimistic Users':<17} {'ARPU':<6} {'Revenue Range (£K)'}")
print("-" * 70)
for i, year in enumerate(years):
    print(f"{year:<6} {conservative_users[i]:<18,} {optimistic_users[i]:<17,} £{arpu[i]:<5} £{conservative_revenue[i]:<6,.0f} - £{optimistic_revenue[i]:,.0f}")

# Cost structure analysis
cost_breakdown = {
    'Cost Category': [
        'AI/ML Development', 'Voice Processing Platform', 'Computer Vision Platform',
        'Clinical Validation', 'Regulatory Compliance', 'Customer Acquisition',
        'Operations & Support', 'Personnel (Technical)', 'Personnel (Clinical)'
    ],
    'Year 1 (£K)': [150, 80, 60, 100, 50, 200, 80, 300, 100],
    'Year 2 (£K)': [200, 120, 100, 150, 30, 500, 150, 600, 200], 
    'Year 3 (£K)': [300, 180, 150, 200, 50, 1000, 300, 1200, 400],
    'Scaling Factor': ['High', 'Medium', 'Medium', 'Low', 'Low', 'High', 'Medium', 'High', 'Medium']
}

df_costs = pd.DataFrame(cost_breakdown)
print(f"\n=== COST STRUCTURE ANALYSIS ===")
print(df_costs.to_string(index=False))

# ROI calculation
print(f"\n=== ROI SCENARIOS ===")
total_costs_y1 = sum(cost_breakdown['Year 1 (£K)'])
total_costs_y2 = sum(cost_breakdown['Year 2 (£K)']) 
total_costs_y3 = sum(cost_breakdown['Year 3 (£K)'])

print(f"Total Costs: Year 1 £{total_costs_y1}K, Year 2 £{total_costs_y2}K, Year 3 £{total_costs_y3}K")
print(f"Break-even Users (Year 3): {total_costs_y3*1000/400:.0f} users at £400 ARPU")
print(f"Conservative Scenario Margin (Year 3): {((conservative_revenue[2]*1000 - total_costs_y3*1000)/(conservative_revenue[2]*1000)*100):.1f}%")
print(f"Optimistic Scenario Margin (Year 3): {((optimistic_revenue[2]*1000 - total_costs_y3*1000)/(optimistic_revenue[2]*1000)*100):.1f}%")