# app.py

import streamlit as st
from utils.file_handler import extract_text_from_pdf, extract_text_from_docx
from utils.text_utils import split_into_sections, generate_download_link
from utils.summarizer import summarize_with_gpt

st.set_page_config(page_title="Text Summarizer", layout="wide")
st.title("📚 Text Summarizer using GPT-4")

uploaded_file = st.file_uploader("Upload a research paper (.pdf or .docx)", type=["pdf", "docx"])
input_text = ""

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    if file_ext == "pdf":
        input_text = extract_text_from_pdf(uploaded_file)
    elif file_ext == "docx":
        input_text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file format.")

    if input_text:
        st.success("Text extracted successfully!")

        if st.button("Generate Summary"):
            with st.spinner("Analyzing and summarizing sections with GPT-4..."):
                sections = split_into_sections(input_text)
                section_summaries = []
                
                for i, section in enumerate(sections):
                    st.info(f"Summarizing section {i+1} of {len(sections)}...")
                    summary = summarize_with_gpt(section)
                    section_summaries.append(summary)

                combined = "\n\n".join([f"Section {i+1} Summary:\n{summary}" for i, summary in enumerate(section_summaries)])
                final_summary = summarize_with_gpt(combined, prompt_instruction="Create a final comprehensive summary of the following section-wise summaries:")

                st.subheader("📝 Final Summary")
                st.write(final_summary)

                st.subheader("📄 Section-wise Summaries")
                for i, sec_summary in enumerate(section_summaries):
                    st.markdown(f"**Section {i+1}**")
                    st.write(sec_summary)

                download_link = generate_download_link(final_summary)
                st.markdown(f"[📥 Download Summary](data:file/txt;base64,{download_link})", unsafe_allow_html=True)

else:
    st.info("Upload a PDF or DOCX file to get started.")
