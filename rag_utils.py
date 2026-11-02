import numpy as np

def chunk_text(text: str, chunk_size: int = 900, overlap: int = 150):
    """Split text into overlapping word-based chunks."""
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Require chunk_size > overlap >= 0.")
    words = text.split()
    chunks = []
    step = chunk_size - overlap
    for start in range(0, len(words), step):
        piece = " ".join(words[start:start + chunk_size]).strip()
        if piece:
            chunks.append(piece)
        if start + chunk_size >= len(words):
            break
    return chunks


def embed_texts(client, texts, batch_size: int = 64):
    """Create embeddings in batches using OpenAI's embedding endpoint."""
    if not texts:
        return np.empty((0, 0), dtype=np.float32)
    vectors = []
    for start in range(0, len(texts), batch_size):
        batch = texts[start:start + batch_size]
        result = client.embeddings.create(
            model="text-embedding-3-small",
            input=batch,
        )
        vectors.extend(item.embedding for item in result.data)
    return np.asarray(vectors, dtype=np.float32)


def retrieve_chunks(query_vector, vectors, chunks, top_k: int = 4):
    """Return the most similar chunks using cosine similarity."""
    if len(chunks) == 0 or len(vectors) == 0:
        return []
    matrix = np.asarray(vectors, dtype=np.float32)
    query = np.asarray(query_vector, dtype=np.float32)
    matrix_norms = np.linalg.norm(matrix, axis=1)
    query_norm = np.linalg.norm(query)
    if query_norm == 0:
        return []
    denominator = matrix_norms * query_norm
    scores = np.divide(
        matrix @ query,
        denominator,
        out=np.zeros_like(matrix_norms),
        where=denominator != 0,
    )
    best_indices = np.argsort(scores)[::-1][:top_k]
    return [chunks[int(index)] for index in best_indices]
