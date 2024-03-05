# LoRA-SpamFilter

A project aimed at filtering spam messages in SMS with miniature language models and part-of-speech tagging techniques. Work with 'gemma:7b' or 'qwen:14b'. 

Note: In the Chinese usage scenario, you need to use the ‘qwen:14b’ model, and in the English scenario, you need to use ‘gemma:7b’

## Consequent

🕐 Under the conditions of more than ten text messages and repeated 5 times, a single message will be responded to in seconds.  
🚦 Achieved 100% accuracy for For English.  
😊 The Chinese recognition logic is still being fine-tuned, so stay tuned.  

![Consequent](/src/Consequent.jpeg)

## install

1. Install 'ollama' on its [official page](https://ollama.com/download) and pip:

```
pip install ollama
```

2. Download Gemma/QWen Full version with ollama:

```bash
ollama pull gemma:7b
ollama pull qwen:14b
```

3. Clone this repo:

```bash
git clone https://github.com/Gloridust/LoRA-SpamFilter.git
```
4. custom model:

```bash
ollama create gemma-7b-spam -f ./modelfile_en
ollama create qwen-14b-spam -f ./modelfile_cn
```

5. Edit code: If you'd like to use with Chinese, you have to edit the code in 'spam_detector.py':

```python
# modelname = 'gemma-7b-spam'
  modelname = 'qwen-14b-spam'
```

6. Run and try it:

```
cd ./LoRA-SpamFilter
python start.py
```

Then you can input SMS to test it.

## Test

Run 'python ./test.py' can test and count the accuracy of results. The program will run the input SMS multiple times and count the results and determine the reasons for each time.

## API

I believe that 'start.py' is the best demo to show how to use 'spam_detector.py'. Just:

```Python
from spam_detector import detect_spam
is_spam,reason = detect_spam(sms_content)
```

'detect_spam' will return two things:

- is_spam: If it is spam?
- reason:Why?

Usually, in scenarios other than debugging, we only use the first parameter 'is_spam'. So you can use it like this:

```
is_spam, _ = detect_spam(sms_content)
```

Enjoy it!

* * *

<a href="https://www.ygeeker.com">
  <img width="180" alt="Sponsored by YGeeker" src="https://www.ygeeker.com/badge/sponsor.png">
</a >
