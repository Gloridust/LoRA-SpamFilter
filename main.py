from llama_cpp import Llama
import json

# Initialize
llm = Llama(
  model_path="./phi-2.Q4_K_M.gguf",
  n_ctx=1024,
  n_threads=4,
  n_gpu_layers=0
)

# User input SMS content
user_input = input("Input your SMS：")

# Build prompt
prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False'. Exclude verification codes from spam. Message: '{user_input}'\nOutput:"

# Execute model inference
output = llm(prompt, max_tokens=512,echo=False)

# Parse model output
try:
    is_spam = output['choices'][0]['text'].strip()  # Adjust based on the actual output structure
    print(f"Spam: {is_spam}")  # Output judgment result
except Exception as e:
    print(f"Error parsing model output: {e}")
