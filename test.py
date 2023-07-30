# Number of people per role
new_business_people = 7
account_manager_people = 8
support_people = 5

# Parameters for roles
new_customer_per_person = 5
churn_reduction_per_person = 5/100
revenue_increase_per_person = 25/100
customers_per_manager = 25
csat_increase_per_person = 1/100
relative_churn_decrease_per_csat_point = 15/100

# Current state of business
current_customers = 1000
monthly_churn_rate = 10/100
monthly_revenue_per_customer = 100

# Calculations
new_customers = new_business_people * new_customer_per_person
account_managed_customers = account_manager_people * customers_per_manager
account_managed_revenue_increase = account_managed_customers * revenue_increase_per_person * monthly_revenue_per_customer
account_managed_churn_decrease = account_managed_customers * churn_reduction_per_person
support_csat_increase = support_people * csat_increase_per_person
support_churn_decrease = current_customers * support_csat_increase * relative_churn_decrease_per_csat_point

# Outputs
total_new_revenue = (new_customers + account_managed_churn_decrease + support_churn_decrease) * monthly_revenue_per_customer + account_managed_revenue_increase

print("The total new monthly revenue is: $", round(total_new_revenue, 2))
