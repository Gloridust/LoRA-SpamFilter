# LoRA-SpamFilter

A project aimed at filtering spam messages in SMS with miniature language models and part-of-speech tagging techniques. Work with Gemma:7b

## Consequent

🕐 Under the conditions of more than ten text messages and repeated 5 times, a single message will be responded to in seconds.
🚦 Achieved 100% accuracy for For English.
😊 The Chinese recognition logic is still being fine-tuned, so stay tuned.

![Consequent](/src/Consequent.jpeg)

## install

1. Install 'ollama' on its [official page](https://ollama.com/download).
2. Download Gemma Full version with ollama:

```bash
ollama pull gemma:7b
```

3. Clone this repo:

```bash
git clone https://github.com/Gloridust/LoRA-SpamFilter.git
```

4. Run and try it:

```
cd ./LoRA-SpamFilter
python start.py
```

Then you can input SMS to test it.

## Test

Run 'python ./test.py' can test and count the accuracy of results. The program will run the input SMS multiple times and count the results and determine the reasons for each time.

## API

To be continued...
