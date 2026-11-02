import numpy as np
import pytest
from rag_utils import chunk_text, retrieve_chunks

def test_chunk_text_returns_overlapping_chunks():
    text = " ".join(f"word{i}" for i in range(12))
    chunks = chunk_text(text, chunk_size=5, overlap=2)
    assert len(chunks) == 4
    assert chunks[0].split()[-2:] == chunks[1].split()[:2]

def test_chunk_text_rejects_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("some text", chunk_size=5, overlap=5)

def test_retrieve_chunks_returns_most_similar_first():
    vectors = np.array([[1, 0], [0, 1], [0.8, 0.2]], dtype=np.float32)
    chunks = [
        {"page": 1, "text": "first"},
        {"page": 2, "text": "second"},
        {"page": 3, "text": "third"},
    ]
    result = retrieve_chunks(np.array([1, 0]), vectors, chunks, top_k=2)
    assert result[0]["text"] == "first"
    assert len(result) == 2

def test_retrieve_chunks_handles_empty_input():
    assert retrieve_chunks(np.array([1, 0]), [], [], top_k=2) == []
