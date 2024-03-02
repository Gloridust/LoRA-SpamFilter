import ollama

def detect_spam(user_input):
    # English
    prompt_en = f"Assess whether the following message is spam or Promotional SMS. Verification code messages should not be considered spam. Output 'True' for spam, 'False' otherwise. Only respond with 'True' or 'False' in one word. Message: '{user_input}'"
    #Chinese
    prompt_cn = f"评估以下消息是否为垃圾邮件或推广类信息。验证码信息不应被视为垃圾信息。输出 'True' 代表垃圾信息或推广类信息，'False' 表示不是。仅用 'True' 或 'False' 单词作答。消息：'{user_input}'"
    # choose_your_language
    prompt = prompt_cn
    # Execute model inference
    model_en = 'gemma:7b'
    model_cn = 'qwen:14b'
    output = ollama.generate(model=model_cn, prompt=prompt)['response']
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
