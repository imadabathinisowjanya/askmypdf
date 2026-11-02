import streamlit as st
import ollama
from pypdf import PdfReader
from rag_utils import chunk_text, embed_texts, retrieve_chunks

st.set_page_config(page_title="AskMyPDF", page_icon="📄", layout="wide")

st.title("📄 AskMyPDF – AI Document Assistant")
st.caption("Ask questions about your PDF using Retrieval-Augmented Generation (RAG).")

with st.sidebar:
    st.header("Settings")
    st.info("Powered by locally running Ollama models. No OpenAI API key required.")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])


def read_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            pages.append({
                "page": page_number,
                "text": text
            })

    return pages


if uploaded_file:
    st.write(f"**Selected document:** {uploaded_file.name}")

    if st.button("Process PDF", type="primary"):
        try:
            with st.spinner("Reading and indexing your PDF..."):
                pages = read_pdf(uploaded_file)

                chunks = []

                for page in pages:
                    for piece in chunk_text(page["text"]):
                        chunks.append({
                            "page": page["page"],
                            "text": piece
                        })

                if not chunks:
                    st.error(
                        "No readable text found. Scanned PDFs may need OCR first."
                    )
                else:
                    vectors = embed_texts(
                        [item["text"] for item in chunks]
                    )

                    st.session_state["chunks"] = chunks
                    st.session_state["vectors"] = vectors
                    st.session_state["filename"] = uploaded_file.name

                    st.success(
                        f"Indexed {len(chunks)} text chunks "
                        f"from {len(pages)} pages."
                    )

        except Exception as exc:
            st.error(f"Could not process this PDF: {exc}")


if "chunks" in st.session_state:
    st.divider()

    st.subheader(
        f"Ask questions about: {st.session_state['filename']}"
    )

    question = st.text_input(
        "Your question",
        placeholder="Example: What are the main findings in this document?"
    )

    if st.button("Ask AI"):
        if not question.strip():
            st.warning("Enter a question first.")

        else:
            try:
                with st.spinner(
                    "Searching the document and generating an answer..."
                ):
                    query_vector = embed_texts([question])[0]

                    relevant = retrieve_chunks(
                        query_vector,
                        st.session_state["vectors"],
                        st.session_state["chunks"],
                        top_k=4
                    )

                    context = "\n\n".join(
                        f"[Page {item['page']}]\n{item['text']}"
                        for item in relevant
                    )

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "Answer using only the supplied document "
                                    "excerpts. If the answer is not present, "
                                    "say you cannot find it in the uploaded "
                                    "document. Cite page numbers."
                                )
                            },
                            {
                                "role": "user",
                                "content": (
                                    f"Question: {question}\n\n"
                                    f"Document excerpts:\n{context}"
                                )
                            }
                        ],
                        options={"temperature": 0.2}
                    )

                st.markdown("### Answer")
                st.write(response["message"]["content"])

                with st.expander("View retrieved document excerpts"):
                    for item in relevant:
                        st.markdown(f"**Page {item['page']}**")
                        st.write(item["text"])

            except Exception as exc:
                st.error(f"Unable to generate an answer: {exc}")


st.divider()
st.caption(
    "Built with Python, Streamlit, Ollama, NumPy, and RAG."
)