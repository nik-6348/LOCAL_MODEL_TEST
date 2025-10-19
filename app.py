import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Page configuration
st.set_page_config(
    page_title="Local AI Chat",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Local AI Chat with GPT-OSS-20B")

# Sidebar for model settings
with st.sidebar:
    st.header("⚙️ Settings")
    max_new_tokens = st.slider("Max New Tokens", min_value=50, max_value=500, value=150, step=10)
    temperature = st.slider("Temperature", min_value=0.1, max_value=2.0, value=0.7, step=0.1)
    top_p = st.slider("Top P", min_value=0.1, max_value=1.0, value=0.9, step=0.05)
    
    st.divider()
    st.caption("Model: openai/gpt-oss-20b")
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize model and tokenizer (cached)
@st.cache_resource
def load_model():
    """Load the model and tokenizer with caching"""
    with st.spinner("Loading model... This may take a few minutes on first run."):
        try:
            tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-20b")
            model = AutoModelForCausalLM.from_pretrained(
                "openai/gpt-oss-20b",
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto" if torch.cuda.is_available() else None,
                low_cpu_mem_usage=True
            )
            
            # Move to GPU if available
            if torch.cuda.is_available():
                st.sidebar.success("✅ GPU Detected")
            else:
                st.sidebar.warning("⚠️ Running on CPU (slower)")
                
            return tokenizer, model
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None, None

# Load model
tokenizer, model = load_model()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    if tokenizer is None or model is None:
        st.error("Model not loaded. Please check the error message above.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            try:
                with st.spinner("Thinking..."):
                    # Prepare messages for the model
                    messages = [{"role": msg["role"], "content": msg["content"]} 
                               for msg in st.session_state.messages]
                    
                    # Apply chat template
                    inputs = tokenizer.apply_chat_template(
                        messages,
                        add_generation_prompt=True,
                        tokenize=True,
                        return_dict=True,
                        return_tensors="pt",
                    ).to(model.device)
                    
                    # Generate response
                    with torch.no_grad():
                        outputs = model.generate(
                            **inputs,
                            max_new_tokens=max_new_tokens,
                            temperature=temperature,
                            top_p=top_p,
                            do_sample=True,
                            pad_token_id=tokenizer.eos_token_id
                        )
                    
                    # Decode the response
                    response = tokenizer.decode(
                        outputs[0][inputs["input_ids"].shape[-1]:],
                        skip_special_tokens=True
                    )
                    
                    # Display response
                    message_placeholder.markdown(response)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
                st.info("If you're running out of memory, try reducing the max tokens or using a GPU.")

# Footer
st.divider()
st.caption("💡 Tip: This app uses the openai/gpt-oss-20b model locally. Make sure you have enough RAM/VRAM.")

