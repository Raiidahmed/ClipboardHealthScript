import numpy as np

# given constants
baseline_churn = 0.10
baseline_customers = 1000
baseline_revenue_per_customer = 100
baseline_new_customers = 25

# functions to calculate new customer, churn and revenue
def calculate_new_customers(nb_personnel):
    return nb_personnel * 5 + baseline_new_customers

def calculate_churn(am_personnel, support_personnel):
    am_reduction = 0.05 * am_personnel
    support_reduction = 0.01 * 0.15 * support_personnel
    total_reduction = am_reduction + support_reduction
    new_churn = max(0, baseline_churn - total_reduction)
    return new_churn

def calculate_revenue(customers, am_personnel):
    return customers * (1 + 0.25 * am_personnel) * baseline_revenue_per_customer

max_revenue = 0
optimal_alloc = (0, 0, 0)

# enforcing a minimum personnel requirement for each role
min_personnel_per_role = 4

roles = ["New Business Acquisition", "Account Management", "Support"]

# check all allocations
for nb_personnel in range(min_personnel_per_role, 21):
    for am_personnel in range(min_personnel_per_role, 21 - nb_personnel):
        support_personnel = 20 - nb_personnel - am_personnel

        if support_personnel < min_personnel_per_role:
            continue

        # calculate customer base and revenue over 12 months
        customers = baseline_customers
        for _ in range(12):
            new_customers = calculate_new_customers(nb_personnel)
            churn = calculate_churn(am_personnel, support_personnel)
            customers = (customers - customers * churn) + new_customers
            revenue = calculate_revenue(customers, am_personnel)

        if revenue > max_revenue:
            max_revenue = revenue
            optimal_alloc = dict(zip(roles, (nb_personnel, am_personnel, support_personnel)))

print(f"Optimal allocation is: ")
for role, personnel in optimal_alloc.items():
    print(f"{role}: {personnel} personnel")
print(f"With max revenue of ${max_revenue}.")
