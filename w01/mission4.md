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
```

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
```

Suppose the model selects:

> **"blue"**

The context now becomes:

> **"The sky is blue"**

The model then uses this new context to predict what should come next.

It might select:

> **"today"**

The process continues:

```text
"The sky is"
      ↓
"The sky is blue"
      ↓
"The sky is blue today"
      ↓
Next token
      ↓
Next token
      ↓
...
```

This means that an LLM can be understood at a basic level as a system that repeatedly predicts what token should come next based on the context available so far.

## 3. My Final Understanding

My understanding is that an LLM does not simply search a database and copy an answer when I give it a prompt.

Instead, the prompt is converted into tokens and processed by the model. The model uses its learned parameters and the context of the prompt to calculate scores for possible next tokens.

A response is then generated step by step. The selected token becomes part of the context used for predicting the next token.

A simplified mental model is:

```text
User Prompt
     ↓
Tokenization
     ↓
Model processes the context
     ↓
Scores for possible next tokens
     ↓
A token is selected
     ↓
Token is added to the context
     ↓
Next token is predicted
     ↓
The process repeats
     ↓
Response
```

Therefore, the key idea I learned is:

> **An LLM generates a response by repeatedly predicting and selecting the next token using the context and the knowledge represented in its learned model parameters.**

## 4. Testing the Explanation

The assignment asks me to check at least two important claims using reliable sources.

### Claim 1 — LLMs use tokens

The first claim is that an LLM does not directly process an entire sentence as ordinary text. The input is divided into tokens that can be processed by the model.

I checked this claim using Hugging Face's documentation about tokenization and language models. The documentation explains how text is converted into tokens before being processed by language models.

**Result:** This claim is supported.

Source:

- [Hugging Face — Tokenization](https://huggingface.co/learn/llm-course/chapter6/5)

### Claim 2 — LLMs can generate text by predicting the next token

The second claim is that an autoregressive language model generates text by predicting the next token using the previous context.

I checked this against Hugging Face's documentation on causal language models and text generation. It explains the next-token generation process used by causal language models.

**Result:** This claim is supported.

Sources:

- [Hugging Face — Causal Language Modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)
- [Hugging Face — Text Generation](https://huggingface.co/docs/transformers/main/en/llm_tutorial)

## 5. One Thing the AI Explained Well

The AI explained **next-token prediction** well.

It helped me understand that an LLM does not generate an entire paragraph as one single step. Instead, it generates the response progressively, predicting the next token based on the context available at that point.

The simple example of completing:

> "The sky is..."

made this concept easier to understand.

## 6. One Thing I Had to Clarify

One clarification I had to make was about what "predicting the next token" actually means.

At first, this phrase could make it sound as though an LLM simply looks up the most common next word from a database.

That is not the correct mental model.

The model uses its learned parameters and processes the available context to produce scores for possible next tokens. The next token is then selected from these possibilities.

Therefore, **next-token prediction is a result of computation using the learned model, not a simple database lookup.**

## 7. Key Learning

The main idea I learned from this investigation is:

```text
Prompt
  ↓
Tokens
  ↓
Context is processed by the model
  ↓
Possible next tokens are scored
  ↓
A token is selected
  ↓
The token becomes part of the context
  ↓
The process repeats
  ↓
Response
```

I do not need to understand all the mathematics of Transformers yet. The important basic mental model is that an LLM processes the prompt as tokens and generates a response progressively by predicting the next token using the context and its learned parameters.

## 8. Sources

1. [Hugging Face — Tokenization](https://huggingface.co/learn/llm-course/chapter6/5)
2. [Hugging Face — Causal Language Modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)
3. [Hugging Face — Text Generation](https://huggingface.co/docs/transformers/main/en/llm_tutorial)
4. [Vaswani et al. — Attention Is All You Need](https://arxiv.org/abs/1706.03762)
