# Function to log test results with variable arguments and keyword arguments
def log_test_result(*test_cases, **details):
    # Print the list of test cases
    print("Logged Test Cases:")
    for test in test_cases:
        print(f"- {test}")

    # Print the details of the test results
    print("\nDetails:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

# Usage example:
# Calling the function with multiple test cases and details as keyword arguments
log_test_result(
    "Login Test", "Signup Test", "No test", 
    payment="Done", status="Passed", execution_time="2.3s", retries=1
)
