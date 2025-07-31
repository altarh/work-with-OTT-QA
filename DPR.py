from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer
import torch
import torch.nn.functional as F


# Load DPR encoders and tokenizers
ctx_tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
ctx_encoder = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")

q_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
q_encoder = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")


def encode_passages(passages):
    inputs = ctx_tokenizer(passages, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = ctx_encoder(**inputs).pooler_output
    return embeddings


def encode_query(query):
    inputs = q_tokenizer(query, return_tensors="pt")
    with torch.no_grad():
        embedding = q_encoder(**inputs).pooler_output
    return embedding


def compute_scores(query_embedding, passage_embeddings):
    return F.cosine_similarity(query_embedding, passage_embeddings)


if __name__ == "__main__":
    # List of strings (documents or file contents)
    documents = ["What is AI?", "Deep learning is a subset of machine learning", "The capital of France is Paris."]

    # Encode all documents
    passage_embeddings = encode_passages(documents)

    # Encode your query
    query = "What is deep learning?"
    query_embedding = encode_query(query)

    # Compute scores
    scores = compute_scores(query_embedding, passage_embeddings)

    # Print sorted results
    for i, (doc, score) in enumerate(sorted(zip(documents, scores), key=lambda x: -x[1]), start=1):
        print(f"{i}. Score: {score:.4f} | Text: {doc}")
