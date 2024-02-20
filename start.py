from spam_detector import detect_spam

# Example SMS content to classify
sms_content = input("Input your SMS：")

# Call the function and print the result
is_spam = detect_spam(sms_content)
print(f"Result:{is_spam}")
