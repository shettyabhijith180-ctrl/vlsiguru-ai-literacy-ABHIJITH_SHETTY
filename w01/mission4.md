# Mission 4 — Make AI explain itself, then test it

## 1. AI Explanation

### First Prompt

I asked an AI assistant:

> "Explain how an LLM produces an answer to my prompt."

The AI explained that when a prompt is given to a Large Language Model (LLM), the text is first broken into smaller pieces called **tokens**. These tokens are converted into numerical representations that the model can process.

The model then processes these representations through its neural-network layers. Modern LLMs commonly use Transformer-based architectures, where attention mechanisms help the model determine which parts of the available context are important.

After processing the context, the model produces scores for possible next tokens. A token is selected based on these scores and added to the existing context. The model then predicts the next token again.

This process is repeated until the model reaches a stopping condition or a generation limit.

Therefore, a simple way to understand LLM generation is:

```text
Prompt
   ↓
Break text into tokens
   ↓
Process the context
   ↓
Predict possible next token
   ↓
Select a token
   ↓
Add the token to the context
   ↓
Predict the next token
   ↓
Repeat
   ↓
Generated response

## 2. Beginner Explanation

### Second Prompt

I then asked the AI:

> "Now explain it to me as a beginner using a simple example."

A simple example is:

> **"The sky is"**

The model looks at the context and considers possible next tokens.

For example:

```text
blue       → high probability
clear      → possible
green      → less likely
car        → very unlikely
