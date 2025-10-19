# AI Chat with Qwen 2.5

A Streamlit-based chat interface for running the Qwen 2.5 (0.5B) model - optimized for Streamlit Cloud deployment.

## Features

- 🤖 Interactive chat interface with chat history
- ⚙️ Adjustable generation parameters (temperature, top-p, max tokens)
- 💾 Session-based conversation memory
- 🚀 GPU acceleration support (automatic fallback to CPU)
- 🎨 Clean and modern UI

## Requirements

- Python 3.10 or 3.11
- 2-4GB RAM (works on Streamlit Community Cloud)
- No GPU required (optimized for CPU)
- ~1GB disk space for model downloads

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

This app uses the `Qwen/Qwen2.5-0.5B-Instruct` model from Hugging Face:
- Model size: ~500 million parameters
- Type: Instruction-tuned causal language model
- Use case: General text generation and chat
- Optimized for: Low-resource environments and cloud deployment

## Performance Tips

- **Cloud-ready**: This model is optimized to run on Streamlit Community Cloud
- **CPU efficient**: Runs smoothly on CPU without GPU acceleration
- **Memory efficient**: Small model size means fast loading and minimal memory usage
- **Reduce tokens**: Lower the "Max New Tokens" setting for faster responses

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

## Deployment

This app is designed to work seamlessly on:
- **Streamlit Community Cloud** (recommended)
- **Local machines** with Python 3.10+
- **Any cloud platform** with minimal resources

### Deploy to Streamlit Cloud:
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Deploy your repository

## License

This project uses the transformers library and the Qwen 2.5 model. Please refer to their respective licenses for usage terms.

## Why Qwen 2.5?

- **Compact**: Only 0.5B parameters, perfect for free cloud hosting
- **Capable**: Instruction-tuned for chat and general tasks
- **Fast**: Quick responses even on CPU
- **Free**: Runs on Streamlit Community Cloud at no cost

