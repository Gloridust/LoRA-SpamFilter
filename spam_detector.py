import ollama

ollama_host = "localhost"
ollama_port = 11434
ollama_model = "gemma:7b"

def detect_spam(user_input):
    prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False' in one word. Message: '{user_input}'"
    # Execute model inference
    output = ollama.generate(model='gemma:7b', prompt=prompt)
    # Parse model output
    is_spam = output['response']
    if "True" in is_spam:
        is_spam= True
        return is_spam
    elif "False" in is_spam:
        is_spam = False
        return is_spam
    else:
        return is_spam
        
if __name__ == "__main__":
    print("You can run 'python start.py' to start.")
