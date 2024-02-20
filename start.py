from spam_detector import detect_spam

# Example SMS content to classify
sms_content = input("Input your SMS：")

# Call the function and print the result
is_spam = detect_spam(sms_content)
print(is_spam)
if is_spam == True:
    print(f"Result: is spam")
elif is_spam == False:
    print(f"Result: not spam")
else:
    print("Error")