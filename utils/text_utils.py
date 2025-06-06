# Splitting and download helpers

def split_into_sections(text: str, max_chars: int = 8000) -> list[str]:
    paragraphs = text.split("\n\n")
    chunks = []
    chunk = ""
    for para in paragraphs:
        if len(chunk) + len(para) < max_chars:
            chunk += para + "\n\n"
        else:
            chunks.append(chunk.strip())
            chunk = para + "\n\n"
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def generate_download_link(summary_text: str) -> str:
    return f"data:text/plain;charset=utf-8,{summary_text.replace('\n', '%0A')}"
