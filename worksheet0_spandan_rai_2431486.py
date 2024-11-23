# -*- coding: utf-8 -*-
"""Worksheet0_Spandan_Rai_2431486.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13uvZyYCugQu8Cz68Qoa8PfVqKKuwffLo

#Task 1

Classify Temperatures:
1. Create empty lists for temperature classifications:

 (a) Cold: temperatures below 10°C.

 (b) Mild: temperatures between 10°C and 15°C.

 (c) Comfortable: temperatures between 15°C and 20°C.
2. Iterate over the temperatures list and add each temperature to the appropriate category.
3. Print the lists to verify the classifications.
"""

# List of temperature readings in Celsius for one month in Kathmandu
# Each day has three readings: night (00-08), evening (08-16), and day (16-24)
temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]

# Create empty lists for temperature classifications
cold = []      # Temperatures below 10°C
mild = []      # Temperatures between 10°C and 15°C
comfortable = []  # Temperatures between 15°C and 20°C

# Iterate over the temperatures and classify them
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)

# Print the lists to verify classifications
print("Cold temperatures:", cold)
print("Mild temperatures:", mild)
print("Comfortable temperatures:", comfortable)

"""

#Task 2

   Based on Data- Answer all the Questions:
 1. How many times was it mild?
 (a) Hint: Count the number of items in the mild list and print the result.
 2. How many times was it comfortable?
 3. How many times was it cold?"""

# Task 1: Classify Temperatures

# List of temperature readings in Celsius for one month in Kathmandu
# Each day has three readings: night (00-08), evening (08-16), and day (16-24)
temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]

# Create empty lists for temperature classifications
cold = []      # Temperatures below 10°C
mild = []      # Temperatures between 10°C and 15°C
comfortable = []  # Temperatures between 15°C and 20°C

# Iterate over the temperatures and classify them
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)

# Print the lists to verify classifications
print("Cold temperatures:", cold)
print("Mild temperatures:", mild)
print("Comfortable temperatures:", comfortable)

# Task 2: Count occurrences in each category
num_cold = len(cold)
num_mild = len(mild)
num_comfortable = len(comfortable)

print("\nNumber of times it was cold:", num_cold)
print("Number of times it was mild:", num_mild)
print("Number of times it was comfortable:", num_comfortable)

"""#Task 3

  Convert Temperatures from Celsius to Fahrenheit

 Using the formula for temperature conversion, convert each reading from Celsius to Fahrenheit and store it in a new list called temperatures_fahrenheit.

 Formula:
 Fahrenheit = (Celsius × 9
 5 ) +32
 1. Iterate over the temperatures list and apply the formula to convert each temperature.
 2. Store the results in the new list.
 3. Print the converted Fahrenheit values
"""

# Task 1: Classify Temperatures

# List of temperature readings in Celsius for one month in Kathmandu
# Each day has three readings: night (00-08), evening (08-16), and day (16-24)
temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]

# Create empty lists for temperature classifications
cold = []      # Temperatures below 10°C
mild = []      # Temperatures between 10°C and 15°C
comfortable = []  # Temperatures between 15°C and 20°C

# Iterate over the temperatures and classify them
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)

# Print the lists to verify classifications
print("Cold temperatures:", cold)
print("Mild temperatures:", mild)
print("Comfortable temperatures:", comfortable)

# Task 2: Count occurrences in each category
num_cold = len(cold)
num_mild = len(mild)
num_comfortable = len(comfortable)

print("\nNumber of times it was cold:", num_cold)
print("Number of times it was mild:", num_mild)
print("Number of times it was comfortable:", num_comfortable)

# Task 3: Convert Temperatures from Celsius to Fahrenheit
# Formula: Fahrenheit = (Celsius × 9/5) + 32
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]

# Print the converted Fahrenheit values
print("\nTemperatures in Fahrenheit:", temperatures_fahrenheit)

"""#Task 4

  Analyze Temperature Patterns by Time of Day:

 Scenario: Each day’s readings are grouped as:

 • Night (00-08),

 • Evening (08-16),

 • Day (16-24).
 1. Create empty lists for night, day, and evening temperatures.
 2. Iterate over the temperatures list, assigning values to each time-of-day list based on their position.
 3. Calculate and print the average day-time temperature.
 4. (Optional) Plot ”day vs. temperature” using matplotlib.
"""

# Importing necessary libraries
import matplotlib.pyplot as plt

# Sample data: Temperatures recorded every hour for a day (24 readings)
temperatures = [15, 14, 13, 12, 14, 13, 12, 13,  # Night (00-08)
                18, 20, 22, 21, 19, 18, 17, 16,  # Evening (08-16)
                20, 21, 23, 24, 22, 21, 19, 18]  # Day (16-24)

# Step 1: Create empty lists for night, evening, and day temperatures
night_temps = []
evening_temps = []
day_temps = []

# Step 2: Assign values to respective lists based on position
for i, temp in enumerate(temperatures):
    if 0 <= i < 8:  # Night (00-08)
        night_temps.append(temp)
    elif 8 <= i < 16:  # Evening (08-16)
        evening_temps.append(temp)
    elif 16 <= i < 24:  # Day (16-24)
        day_temps.append(temp)

# Step 3: Calculate and print the average daytime temperature
if day_temps:
    avg_day_temp = sum(day_temps) / len(day_temps)
    print(f"Average daytime temperature: {avg_day_temp:.2f}°C")
else:
    print("No daytime temperatures available to calculate the average.")

# Step 4: Optional: Plot "day vs. temperature" using matplotlib
plt.plot(range(len(day_temps)), day_temps, marker='o', label="Day Temperatures")
plt.xlabel("Hour (16:00 - 24:00)")
plt.ylabel("Temperature (°C)")
plt.title("Day vs. Temperature")
plt.grid(True)
plt.legend()
plt.show()

"""#Task 1

 Sum of Nested Lists:

 Scenario: You have a list that contains numbers and other lists of numbers (nested lists).
 You want to find the total sum of all the numbers in this structure.
 Task:
 • Write a recursive function sum_nested_list(nested_list) that:
 1. Takes a nested list (a list that can contain numbers or other lists of numbers) as
 input.
 2. Sums all numbers at every depth level of the list, regardless of how deeply nested
 the numbers are.
 • Test the function with a sample nested list, such as
 nested_list = [1, [2, [3, 4], 5], 6, [7, 8]].
 The result should be the total sum of all the numbers

"""

def sum_nested_list(nested_list):
    """
    Recursively calculates the sum of all numbers in a nested list.

    :param nested_list: A list containing numbers or other lists of numbers.
    :return: Total sum of all numbers.
    """
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):  # If the element is a list, call the function recursively
            total_sum += sum_nested_list(element)
        else:  # If the element is a number, add it to the sum
            total_sum += element
    return total_sum

# Test the function with a sample nested list
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print(f"The total sum of all numbers in the nested list is: {result}")

"""#Task 2

 Generate All Permutations of a String:

 Scenario:Given a string, generate all possible per mutations of its characters. This is useful
 forunder standing back tracking and recursive depth-first search.
 Task:

 •Write are cursive function generate_permutations(s)that:

 –Takes a strings as input an dreturnsalist of all uniqueper mutations.

 •Test with strings like”abc”and”aab”.

 print(generate_permutations("abc"))
 #### Should return [’abc’, ’acb’, ’bac’, ’bca’,’cab’, ’cba’]
"""

def generate_permutations(s):
    """
    Generates all unique permutations of a string using recursion.

    :param s: The input string.
    :return: A list of unique permutations.
    """
    # Base case: if the string is empty or has one character, return it as the only permutation
    if len(s) <= 1:
        return [s]

    # Recursive case: generate permutations by selecting each character as the start
    permutations = []
    for i, char in enumerate(s):
        # Avoid duplicate permutations for repeated characters
        if char in s[:i]:
            continue
        # Remaining string after removing the current character
        remaining = s[:i] + s[i+1:]
        # Generate permutations for the remaining string
        for perm in generate_permutations(remaining):
            permutations.append(char + perm)

    return permutations

# Test the function with example strings
print("Permutations of 'abc':", generate_permutations("abc"))
print("Permutations of 'aab':", generate_permutations("aab"))

"""#Task 3

 Directory Size Calculation:
 1. Write a recursive function calculate_directory_size(directory) where:
 • directory is a dictionary where keys represent file names (with values as sizes in
 KB) or directory names (with values as another dictionary representing a subdi
rectory).
 • The function should return the total size of the directory, including all nested
 subdirectories.
 2. Test the function with a sample directory structure.
"""

def calculate_directory_size(directory):
    """
    Recursively calculates the total size of a directory, including nested subdirectories.

    :param directory: A dictionary representing the directory structure.
                      Keys are file or directory names.
                      Values are file sizes (in KB) or subdirectory dictionaries.
    :return: Total size of the directory in KB.
    """
    total_size = 0
    for name, value in directory.items():
        if isinstance(value, dict):  # If the value is a subdirectory, calculate its size recursively
            total_size += calculate_directory_size(value)
        else:  # If the value is a file size, add it to the total size
            total_size += value
    return total_size

# Sample directory structure for testing
sample_directory = {
    "file1.txt": 500,
    "file2.txt": 1200,
    "subdir1": {
        "file3.txt": 700,
        "file4.txt": 300,
        "subsubdir1": {
            "file5.txt": 100,
            "file6.txt": 200,
        },
    },
    "subdir2": {
        "file7.txt": 400,
    },
}

# Test the function
total_size = calculate_directory_size(sample_directory)
print(f"The total size of the directory is: {total_size} KB")

"""#Task 1

 Exercises- Dynamic Programming:

  Coin Change Problem:
  
 Scenario: Given a set of coin denominations and a target amount, find the minimum number
 of coins needed to make the amount. If it’s not possible, return- 1.
 Task:
 1. Write a function min_coins(coins, amount) that:
 • Uses DP to calculate the minimum number of coins needed to make up the
 amount.
 2. Test with coins = [1, 2, 5] and amount = 11. The result should be 3 (using coins
 [5, 5, 1])
"""

def min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up the given amount using DP.

    :param coins: List of coin denominations.
    :param amount: The target amount.
    :return: Minimum number of coins needed, or -1 if it's not possible.
    """
    # Initialize the DP array with a high value (infinity-like)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: no coins are needed to make amount 0

    # Build the DP table
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[amount] is still 'inf', the amount cannot be made with given coins
    return dp[amount] if dp[amount] != float('inf') else -1

# Test the function
coins = [1, 2, 5]
amount = 11
result = min_coins(coins, amount)
print(f"Minimum number of coins needed to make {amount}: {result}")

"""#Task 2

LongestCommonSubsequence(LCS):

 Scenario: Given two strings, find the length of their longest common subsequence(LCS).
 This is useful in text comparison.
 Task:
 1. Write a function longest_common_subsequence(s1,s2)that:
 •Uses DP to find the length of the LCS of two strings s1and s2.
 2. Test with strings like "abcde" and "ace";the LCS length should be 3 ("ace").
"""

def longest_common_subsequence(s1, s2):
    """
    Finds the length of the longest common subsequence (LCS) between two strings using DP.

    :param s1: First string.
    :param s2: Second string.
    :return: Length of the LCS.
    """
    # Create a DP table with dimensions (len(s1)+1) x (len(s2)+1)
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Fill the DP table
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]

# Test the function
s1 = "abcde"
s2 = "ace"
result = longest_common_subsequence(s1, s2)
print(f"Length of the LCS between '{s1}' and '{s2}': {result}")

"""#Task 3- 0/1

  Knapsack Problem:
  
 Scenario: You have a list of items, each with a weight and a value. Given a weight capacity, maximize the total value of items you can carry without exceeding the weight capacity.
 Task:
 1. Write a function knapsack(weights, values, capacity) that:
 • Uses DP to determine the maximum value that can be achieved within the given
 weight capacity.
 2. Test with weights [1, 3, 4, 5], values [1, 4, 5, 7], and capacity 7.  The result should be 9.
"""

def knapsack(weights, values, capacity):
    """
    Solves the 0/1 Knapsack Problem using DP to maximize the value within the given capacity.

    :param weights: List of weights of the items.
    :param values: List of values of the items.
    :param capacity: Maximum weight capacity of the knapsack.
    :return: Maximum value that can be achieved within the given capacity.
    """
    n = len(weights)
    # DP table where dp[i][w] represents the maximum value that can be obtained with
    # the first i items and weight capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If the item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # If the item cannot be included
                dp[i][w] = dp[i - 1][w]

    # The value at dp[n][capacity] is the maximum value that can be achieved
    return dp[n][capacity]

# Test the function
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
result = knapsack(weights, values, capacity)
print(f"Maximum value that can be achieved with capacity {capacity}: {result}")

