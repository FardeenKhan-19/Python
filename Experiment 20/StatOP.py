'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
import numpy as np

# Function to calculate and display statistical measures
def calculate_statistics(data):
    # Convert the input data to a NumPy array
    data_array = np.array(data)

    # Calculate mean
    mean_value = np.mean(data_array)
    print(f"Mean: {mean_value}")

    # Calculate median
    median_value = np.median(data_array)
    print(f"Median: {median_value}")

    # Calculate variance
    variance_value = np.var(data_array)
    print(f"Variance: {variance_value}")

    # Calculate standard deviation
    std_deviation_value = np.std(data_array)
    print(f"Standard Deviation: {std_deviation_value}")

    data_array2 = np.array(data)

    # For correlation coefficients, we need at least two variables
    #if data_array.ndim > 1 and data_array.shape[0] > 1:
    correlation_matrix = np.corrcoef(data_array,data_array2)
    print(f"Correlation Coefficients:\n{correlation_matrix}")

# Main function to handle user input
def main():
    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")

    try:
        # Convert the user input into a list of floats
        data = list(map(float, user_input.split()))

        # Call the function with the user-provided data
        calculate_statistics(data)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

    