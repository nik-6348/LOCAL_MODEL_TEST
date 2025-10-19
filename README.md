# Local AI Chat with GPT-OSS-20B

A Streamlit-based chat interface for running the OpenAI GPT-OSS-20B model locally on your machine.

## Features

- 🤖 Interactive chat interface with chat history
- ⚙️ Adjustable generation parameters (temperature, top-p, max tokens)
- 💾 Session-based conversation memory
- 🚀 GPU acceleration support (automatic fallback to CPU)
- 🎨 Clean and modern UI

## Requirements

- Python 3.8 or higher
- At least 16GB RAM (32GB+ recommended for this large model)
- GPU with 40GB+ VRAM recommended (model is ~240GB in size)
- Sufficient disk space for model downloads

## Installation

1. Clone or download this project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

## Usage

1. The app will automatically download the model on first run (this may take a while)
2. Type your message in the chat input at the bottom
3. Adjust generation settings in the sidebar:
   - **Max New Tokens**: Maximum length of generated responses
   - **Temperature**: Controls randomness (higher = more creative)
   - **Top P**: Nucleus sampling parameter
4. Click "Clear Chat History" to start a new conversation

## Model Information

This app uses the `openai/gpt-oss-120b` model from Hugging Face:
- Model size: ~120 billion parameters
- Type: Causal language model
- Use case: General text generation and chat

## Performance Tips

- **GPU recommended**: This is a very large model. A GPU with sufficient VRAM will significantly improve performance
- **CPU mode**: If running on CPU, expect slower response times
- **Memory**: Close other applications to free up memory
- **Reduce tokens**: Lower the "Max New Tokens" setting if experiencing memory issues

## Troubleshooting

### Out of Memory Error
- Reduce the "Max New Tokens" setting
- Close other applications
- Consider using a smaller model if your hardware is limited

### Model Download Issues
- Ensure you have a stable internet connection
- Check that you have sufficient disk space
- The model files are large and may take time to download

### Slow Performance
- Use a GPU if available
- Reduce the max tokens setting
- Consider using quantized versions of the model (requires additional setup)

## Note

The GPT-OSS-120B model is extremely large and requires substantial computational resources. If you encounter performance issues, consider:
- Using a smaller model (e.g., GPT-2, smaller LLaMA models)
- Using model quantization (4-bit or 8-bit)
- Running on cloud GPU instances

## License

This project uses the transformers library and the OpenAI GPT-OSS-120B model. Please refer to their respective licenses for usage terms.

