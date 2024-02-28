from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallHandler

ollama_host = "localhost"
ollama_port = 11434
ollama_model = "gemma:7b"

def detect_spam(user_input):
    
    prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False' in one word. Message: '{user_input}'"
    llm = Ollama(base_url=f"http://{ollama_host}:{ollama_port}", 
        model=ollama_model,
        callback_manager=CallbackManager([StreamingStdOutCallHandler()])
        )
    # Execute model inference
    output = llm(prompt, max_tokens=128, echo=False)
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
