# RAG Retrieval With Citations

## Pattern

Webhook-driven retrieval augmented generation. A caller sends a query, the workflow embeds it, retrieves relevant records, and returns an answer with source references attached.

## Flow

Webhook In -> Embed Query with OpenAI -> Query Pinecone -> OpenAI Completion with Citations -> Format Response.

## Useful For

Internal knowledge bases, support-document search, policy lookup, onboarding assistants, and any workflow where the answer needs attribution.

## Setup Notes

Reconnect OpenAI and vector database credentials after import. Replace the Pinecone endpoint, namespace, and metadata fields with the structure from your own corpus before testing with real users.

## Validation Focus

The workflow keeps the retrieval and answer steps separate, which makes it easier to inspect missed retrievals separately from poor generation.
