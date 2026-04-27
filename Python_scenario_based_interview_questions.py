# Python scenario based interview questions
# Question 1: Input String: text = "Analytics2026". Extract only the digits from the string (remove letters and other characters)
# Expected Output: 2026

text = "Analytics2026"

digits_only = ''.join([char for char in text if char.isdigit()])
print(digits_only)

# Output: 2026
