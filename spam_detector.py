import ollama

def detect_spam(user_input):
    prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False' in one word. Message: '{user_input}'"
    # Execute model inference
    output = ollama.generate(model='gemma:7b', prompt=prompt)['response']
    # Parse model output
    is_spam = output
    if "True" in output:
        is_spam= True
        return (is_spam,output)
    elif "False" in output:
        is_spam = False
        return (is_spam,output)
    else:
        return (is_spam,output)
        
if __name__ == "__main__":
    print("You can run 'python start.py' to start.")
