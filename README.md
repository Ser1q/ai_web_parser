# ai_web_parser
---
````markdown
# 🧠 AI Web Parser

A Python-based project that uses a fine-tuned **DeepSeek Coder R1.3B** model to intelligently parse data from webpages and adapt to changing HTML structures. Ideal for automating data extraction tasks from dynamic websites.

## 🚀 Features

- 🤖 Uses **DeepSeek Coder R1.3B** (open-weight LLM) for robust HTML parsing.
- 📄 Adapts to webpage structure changes using few-shot prompting.
- 🔧 Supports input of old HTML, old code, and new HTML to generate updated code.
- 🧪 Simple CLI interface to test and generate Python parsers for new web content.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Ser1q/ai_web_parser.git
cd ai_web_parser
````

Install required packages:

```bash
pip install -r requirements.txt
```

Make sure you have `deepseek-coder-1.3b-base` or compatible model downloaded locally or accessible via HuggingFace.

## 🛠 Usage

To generate Python parsing code using a few-shot prompt approach:

```bash
python generate_code.py \
    --old_html examples/old.html \
    --old_code examples/old_code.py \
    --new_html examples/new.html \
    --output new_code.py
```

Example prompt template (from `generate_code.py`):

```python
template = (
    "You are tasked with writing a specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}.\n"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.\n"
    "3. **Empty Response:** If no information matches the description, return an empty string ('').\n"
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested."
)
```

## 🤖 Model Notes

This project uses [DeepSeek Coder](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base), a 1.3B parameter LLM trained on code and natural language, ideal for code generation and HTML parsing tasks.

If you don't have access to DeepSeek locally, you can try running inference via [Transformers](https://github.com/huggingface/transformers) or use `text-generation-webui` for testing.

## ✅ TODO

* [ ] Support multi-page parsing
* [ ] Fine-tune DeepSeek with custom examples

## 📄 License

MIT License. See [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Developed by [@Ser1q](https://github.com/Ser1q)

