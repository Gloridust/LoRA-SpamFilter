from llama_cpp import Llama

def detect_spam(user_input):
    # Initialize Llama model
    llm = Llama(
      model_path="./phi-2.Q4_K_M.gguf",
      n_ctx=256,
      n_threads=4,
      n_gpu_layers=0
    )

    # Build prompt
    prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False' in one word. Message: '{user_input}'"

    # Execute model inference
    output = llm(prompt, max_tokens=64, echo=False)
    # Parse model output
    is_spam = output['choices'][0]['text'].strip()  # Adjust based on the actual output structure
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
