from spam_detector import detect_spam

# Example SMS content to classify
sms_content = input("Input your SMS：")

# Call the function and print the result
is_spam = detect_spam(sms_content)
if is_spam == True:
    print(f"Result: is spam")
else:
    print(f"Result: not spam")