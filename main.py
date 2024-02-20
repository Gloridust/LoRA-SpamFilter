from llama_cpp import Llama
import json

# 初始化模型
llm = Llama(
  model_path="./phi-2.Q4_K_M.gguf",
  n_ctx=512,
  n_threads=1,
  n_gpu_layers=0
)

# 用户输入短信内容
user_input = input("Input your SMS：")

# 构建prompt
prompt = f"Assess whether the following message is spam. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False'. Exclude verification codes from spam. Message: '{user_input}'\nOutput:"


# 执行模型推理
output = llm(prompt, max_tokens=512,echo=False)

# 解析模型输出
try:
    is_spam = output['choices'][0]['text'].strip()  # 根据实际输出结构调整
    print(f"Spam: {is_spam}")  # 输出判断结果
except Exception as e:
    print(f"Error parsing model output: {e}")

