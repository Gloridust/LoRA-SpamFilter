import ollama

def detect_spam(user_input):
    modelname = 'gemma-7b-spam'
    # modelname = 'qwen-14b-spam'
    output = ollama.generate(model=modelname, prompt=user_input)['response']
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
    print("Run 'python start.py' to start.")
