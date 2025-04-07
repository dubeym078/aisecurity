LLM Guard flow
# Architecture Diagram

```mermaid
graph TD;
    A[User] -->|Provides prompt| B[openai_api.py]
    B -->|Environment Variable| C[os.getenv("OPENAI_API_KEY")]
    B -->|Initialize| D[OpenAI Client]
    B -->|Initialize| E[Vault]
    B -->|Create| F[Input Scanners]
    B -->|Create| G[Output Scanners]
    B -->|Scan| H[scan_prompt]
    H -->|Sanitized Prompt, Results| B
    B -->|Check Validation| I[Results Valid]
    I -->|Valid| J[Create Completion]
    J -->|Prompt| K[OpenAI API]
    K -->|Response| L[Completion Response]
    L -->|Scan| M[scan_output]
    M -->|Sanitized Response, Results| B
    B -->|Check Validation| N[Results Valid]
    N -->|Valid Output| O[Print Output]

    classDef openai fill:#f96;
    D, K, L -->|OpenAI API| class:openai
    classDef vault fill:#69f;
    E -->|Vault| class:vault
    classDef scanner fill:#6f9;
    F, G, H, M -->|Scanners| class:scanner
