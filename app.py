import streamlit as st
from transformers import pipeline

# ✅ Load the Transformer summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Set page configuration
st.set_page_config(page_title="Text Summarizer", layout="centered")
st.markdown(
    "<h2 style='text-align: center; color: #4CAF50;'>📝 AI Text Summarizer</h2>", unsafe_allow_html=True
)

# Layout: sliders + text area
col1, col2 = st.columns(2)
with col1:
    max_len = st.slider("🔝 Max Summary Length", 50, 300, 100)
with col2:
    min_len = st.slider("🔽 Min Summary Length", 20, 80, 30)

# Input box
input_text = st.text_area("✍️ Your Text:", height=200, max_chars=2000)
st.caption(f"Characters typed: {len(input_text)}")

# Button to summarize
if st.button("🚀 Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarizer(input_text, max_length=max_len, min_length=min_len, do_sample=False)
            st.success("✅ Summary generated!")

            # Show original text collapsed
            with st.expander("🔎 Original Text"):
                st.write(input_text)

            # Show summary in copyable format
            st.subheader("📃 Summary:")
            st.code(summary[0]['summary_text'], language="text")
