# W01 Python Program: Setup Slack Checker
# Purpose: Calculate simplified setup slack and report its status.

print("=== Setup Slack Checker ===")

arrival_time = float(input("Enter data arrival time (ns): "))
required_time = float(input("Enter required time (ns): "))

setup_slack = required_time - arrival_time

print("\n--- Timing Results ---")
print("Data arrival time:", arrival_time, "ns")
print("Required time:", required_time, "ns")
print("Setup slack:", setup_slack, "ns")

if setup_slack > 0:
    print("Status: Positive setup slack")
elif setup_slack == 0:
    print("Status: Zero setup slack")
else:
    print("Status: Setup timing violation")
