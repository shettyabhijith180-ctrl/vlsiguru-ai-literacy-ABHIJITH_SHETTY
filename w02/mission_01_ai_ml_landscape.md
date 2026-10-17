# Mission 1 — Build the AI and ML Landscape

## 1. Introduction

Artificial Intelligence (AI) is a broad field of computer science that focuses on building systems capable of performing tasks that normally require intelligent behaviour.

Machine Learning (ML) is a part of AI in which computer systems learn patterns from data and use those patterns to make predictions or generate outputs.

In traditional programming, developers explicitly write rules for the computer to follow. In machine learning, an algorithm uses training data to learn patterns that can be applied to new examples.

Understanding the differences between these approaches helps engineers decide which technique is appropriate for a particular problem.

---

## 2. Concept Map: AI and Machine Learning

The following concept map shows how AI, Machine Learning, Deep Learning, Generative AI, and Large Language Models are related.

```text
                    ARTIFICIAL INTELLIGENCE (AI)
                    Broad field of intelligent systems
                                |
                +---------------+----------------+
                |                                |
       Rule-Based Systems                 Machine Learning (ML)
       Explicitly programmed              Learns patterns from data
                |                                |
       Follows predefined rules          +-------+---------+
                                         |                 |
                                   Other ML Methods   Deep Learning
                                                     Neural networks
                                                     with multiple layers
                                                            |
                                                Many modern Generative AI
                                                systems use deep learning

                    GENERATIVE AI
                    Generates new content
                    such as text, images, or code
                                |
                    Large Language Models (LLMs)
                    Process and generate language
                    Many modern LLMs use Transformers
```

**Important clarification:** This is a simplified conceptual map, not a strict hierarchy. Generative AI describes the ability to generate content, while Deep Learning describes a family of machine-learning methods. Many modern Generative AI systems use deep learning, but these terms do not mean the same thing. LLMs are specialised language models, and many modern LLMs use Transformer architectures.

### Explanation of the concept map

- **Artificial Intelligence (AI):** The broad field concerned with creating systems that perform tasks requiring intelligent behaviour.
- **Machine Learning (ML):** An approach within AI in which models learn patterns from data.
- **Deep Learning:** A type of ML that uses neural networks with multiple layers to learn complex patterns.
- **Generative AI:** AI systems that generate new content, such as text, images, audio, or code.
- **Large Language Models (LLMs):** Models designed to process and generate language. Many modern LLMs use deep-learning architectures based on Transformers.

---

## 3. Five Important Distinctions

### Distinction 1: Artificial Intelligence vs Machine Learning

AI is the broader field, while ML is one approach used to build AI systems.

For example, a system that follows predefined rules to detect a timing violation can be an AI-related automation or conventional rule-based system, depending on how the application is defined. An ML model, in contrast, can learn patterns from historical design data to predict whether a new design run may fail timing.

Therefore, AI and ML are related, but they are not interchangeable terms.

### Distinction 2: Rule-Based Programming vs Machine Learning

In rule-based programming, a developer explicitly defines the conditions and actions.

For example:

```text
IF setup slack < 0:
    Report setup timing violation
ELSE:
    Report timing pass
```

The program follows the written condition.

In machine learning, a model learns patterns from examples. For instance, an ML model could use historical physical design data to estimate whether a new design is likely to pass timing.

Rule-based programming is useful when the rules are known and reliable. ML may be useful when patterns are difficult to describe using fixed rules and suitable training data is available.

### Distinction 3: Machine Learning vs Deep Learning

Machine Learning includes different methods for learning patterns from data.

Deep Learning is a type of ML that uses neural networks with multiple layers.

For example, a traditional ML method might predict power consumption from selected design measurements. A deep-learning model could also learn relationships in data, potentially handling more complex patterns when sufficient suitable data and computing resources are available.

Deep Learning is therefore part of Machine Learning, not a completely separate field.

### Distinction 4: Deep Learning vs Generative AI

Deep Learning describes a family of methods based on neural networks with multiple layers.

Generative AI describes systems that create new content, such as text, images, or code.

Many modern Generative AI systems use deep-learning models. However, the terms describe different things: one refers to a modelling approach, while the other refers to a system's content-generation capability.

For example, a deep-learning model could classify an image, while a generative model could create a new image.

### Distinction 5: Generative AI vs Large Language Models

Generative AI is a broad category of AI systems that generate content. This content may include text, images, audio, video, or code.

Large Language Models are designed to process and generate language. Many modern LLMs are used in Generative AI applications such as chatbots, technical explanations, and code assistance.

For example, an LLM can help a Physical Design engineer understand a Tcl script or explain a timing report. However, its explanation must be checked before it is used in actual engineering work.

An LLM is therefore one kind of model that can be used for Generative AI, but Generative AI is not limited to LLMs.

---

## 4. Three Examples and Their Classification

### Example 1: Rule-Based Setup Timing Check

**Problem:** Identify whether a reported setup slack indicates a timing violation.

**Method:** A program checks whether setup slack is negative.

```text
Input: Setup slack

IF setup slack < 0:
    Report setup timing violation
ELSE:
    Report timing pass
```

**Classification:** Rule-based programming / conventional software.

**Reason:** The programmer explicitly defines the condition. The program does not need to learn from training data to perform this check.

**Limitation:** The rule only checks the supplied slack value. It does not independently perform a complete static timing analysis or identify the underlying cause of the violation.

### Example 2: Predicting Timing Pass or Fail

**Problem:** Estimate whether a new physical design run is likely to pass timing.

**Method:** Train an ML model using suitable historical design-run data, such as cell count, congestion measurements, and known timing outcomes.

**Classification:** Machine Learning, potentially supervised classification.

**Reason:** The model learns patterns from examples that include known outcomes and predicts a category, such as pass or fail, for a new design run.

**Limitation:** The prediction may be unreliable if the training data is insufficient, inaccurate, or unrepresentative of the new design. The model's performance must be evaluated on appropriate unseen data.

### Example 3: An LLM Explaining a Tcl Script

**Problem:** Understand a Tcl script used in a Physical Design workflow.

**Method:** Ask an LLM to explain the commands, describe the script's intended behaviour, and identify possible issues.

**Classification:** Generative AI using a Large Language Model.

**Reason:** The model generates a natural-language explanation based on the supplied script and prompt.

**Limitation:** The explanation may contain incorrect assumptions or misunderstand the tool-specific commands. The engineer must inspect the script and verify its behaviour before using it.

---

## 5. Is Automation Always AI?

No. Automation does not necessarily involve AI or machine learning.

For example, a script that automatically checks setup slack and prints a warning follows explicitly programmed rules. It is automated, but it does not learn patterns from data.

An ML system, on the other hand, may learn from historical design runs to predict the likelihood of a timing failure.

Therefore, automation describes the execution of tasks with reduced manual intervention, while AI refers to a broader set of techniques for performing tasks associated with intelligent behaviour.

Similarly, AI does not always require ML. Some systems use predefined rules rather than learned models.

---

## 6. Key Learning

The most important thing I learned is that AI, Machine Learning, Deep Learning, Generative AI, and LLMs are related concepts, but they do not all describe the same type of technology.

AI is the broad field. ML is an approach that learns patterns from data, and Deep Learning is a type of ML based on neural networks with multiple layers.

Generative AI refers to systems that create new content, while LLMs are specialised models for processing and generating language.

I also learned that a conventional rule-based solution may be more appropriate than ML when the problem can be solved reliably using a simple, clearly defined condition.

As a VLSI Physical Design student, I can connect these concepts to timing checks, power estimation, design optimisation, and the use of LLMs to understand engineering scripts.

---

## 7. Sources and What They Support

### Source 1 — Google: Introduction to Machine Learning

Link: https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

**What it supports:** The definition of machine learning, how ML differs from traditional programming, and the basic ideas behind supervised learning, unsupervised learning, and Generative AI.

### Source 2 — IBM: What Is Machine Learning?

Link: https://www.ibm.com/think/topics/machine-learning

**What it supports:** The relationship between AI and ML, the role of training data, the purpose of learned models, and the relationship between ML and Deep Learning.

### Source 3 — Google: Machine Learning Crash Course

Link: https://developers.google.com/machine-learning/crash-course/

**What it supports:** Additional introductory explanations of machine-learning models, classification, regression, data, and model evaluation.

I used these sources to check the basic concepts and then explained them in my own words. The VLSI examples are illustrative applications intended to show how the concepts could be used in Physical Design.
