from spam_detector import detect_spam

# Example SMS content to classify
sms_content = input("Test your SMS: ")

# Initialize counters
true_count = 0
false_count = 0

# Repeat the detection process 10 times
for _ in range(5):
    is_spam = detect_spam(sms_content)
    if is_spam:
        true_count += 1
    else:
        false_count += 1

# Print the counts
print(f"Number of times classified as spam: {true_count}")
print(f"Number of times classified as not spam: {false_count}")
