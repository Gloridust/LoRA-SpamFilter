from llama_cpp import Llama

def detect_spam(user_input):
    # Initialize Llama model
    llm = Llama(
      model_path="./phi-2.Q4_K_M.gguf",
      n_ctx=1024,
      n_threads=4,
      n_gpu_layers=0
    )

    # Build prompt
    prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False' in one word.Message: '{user_input}'"

    # Execute model inference
    output = llm(prompt, max_tokens=1024, echo=False)
    # Parse model output
    try:
        is_spam = output['choices'][0]['text'].strip()  # Adjust based on the actual output structure
        if "True" in is_spam:
            is_spam= True
        elif "False" in is_spam:
            is_spam = False
        else:
            return None
        return is_spam
    except Exception as e:
        print(f"Error parsing model output: {e}")
        return None

if __name__ == "__main__":
    print("You can run 'python start.py' to start.")
