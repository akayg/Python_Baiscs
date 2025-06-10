def calculate_average(*args):
    """
    Calculate the average of variable arguments.

    Args:
        *args: Variable number of numerical arguments.

    Returns:
        float: The average of the arguments. Returns 0 if no arguments are provided.
    """
    if not args:
        return 0
    return sum(args) / len(args)

# Example usage
if __name__ == "__main__":
    print(calculate_average(10, 20, 30))  # Output: 20.0
    print(calculate_average())           # Output: 0