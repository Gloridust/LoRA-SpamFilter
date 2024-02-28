from spam_detector import detect_spam

# Example SMS content to classify
sms_content = input("Test your SMS: ")

# Initialize
true_count = 0
false_count = 0
error_count = 0
error_text = ''

# Repeat the detection process 10 times
for _ in range(5):
    is_spam = detect_spam(sms_content)
    if is_spam == True:
        true_count += 1
    elif is_spam == False:
        false_count += 1
    else:
        error_count += 1
        error_text += (str(error_count) + is_spam)

# Print the counts
print(f"Number of times classified as spam: {true_count}")
print(f"Number of times classified as not spam: {false_count}")
print(f"Number of times classified as error: {error_count}\n{error_text}")
