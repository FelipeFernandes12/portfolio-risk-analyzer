"""for num in range(10, 21):
    print(f"Auditing record number: {num}")"""

"""account_ids = [101, 404, 202, 999, 303, 404]
for account_id in account_ids:
    if account_id == 404:
        print("ID 404: WARNING - Suspicious activity flagged!")
    elif account_id == 999:
        print("ID 999: CRITICAL - Access Denied!")
    else:
        print(f"ID {account_id}: Cleared.")"""

system_status = {
    "Database": "Online",
    "API_Gateway": "Overloaded",
    "Auth_Server": "Online",
    "Storage_Bucket": "Offline"
}

# 1. Loop through both keys (system) and values (status)
"""for system, status in system_status.items():

    
    # 2. Check the value stored in the 'status' variable
    if status == "Online":
        print(f"System {system} is running perfectly. ")
    else:
        print(f"System {system} requires attention! Status: {status} ")"""

training_status = {
    "Alice": "Complete",
    "Bob": "Pending",
    "Charlie": "Complete",
    "David": "Expired"
}

for employee, status in training_status.items():
    if status == "Complete":
        print(f"Access granted to {employee}.")
    else:
        print(f"Access denied for {employee}. Training status: {status}.")