# Mission 6 — Chatbot or agent?

## 1. Understanding the Key Concepts

Mission 6 focuses on understanding the difference between an LLM, an AI application, RAG, a tool-using assistant, and an agent.

These systems can all use AI models, but they differ in what they can do beyond simply generating an answer.

---

## 2. LLM

**LLM** stands for **Large Language Model**.

An LLM is a model trained on a large amount of text data that can understand and generate human-like text.

It can perform tasks such as:

- Answering questions
- Explaining concepts
- Summarizing text
- Generating code
- Writing content

A simple mental model is:

```text
User Prompt
     ↓
    LLM
     ↓
Generated Response
```

The LLM itself mainly processes the input and generates an output. It does not automatically mean that the system can access external tools or take actions.

---

## 3. AI Application

An **AI application** is a software application that uses an AI model to provide a useful functionality to the user.

The application can contain an LLM along with other software components such as a user interface, databases, APIs, and application logic.

For example, a chatbot application can use an LLM to answer questions.

A simplified structure is:

```text
User
  ↓
AI Application
  ↓
LLM
  ↓
Response
  ↓
User
```

Therefore, an AI application is broader than just the underlying LLM.

---

## 4. RAG

**RAG** stands for **Retrieval-Augmented Generation**.

RAG allows an AI system to retrieve relevant information from an external knowledge source and provide that information as context to the model before generating an answer.

A simple RAG workflow is:

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Retrieved Context
      ↓
LLM
      ↓
Generated Answer
```

For example, if a company has a collection of internal documents, a RAG system can retrieve relevant information from those documents and use it to answer an employee's question.

The important idea is:

> **RAG adds external information to the context used by the model.**

---

## 5. Tool-Using Assistant

A **tool-using assistant** is an AI system that can use external tools to obtain information or perform specific operations.

Examples of tools include:

- Calculator
- Web search
- Database
- Calendar
- Email service
- Weather service

A simple workflow is:

```text
User Request
      ↓
     Model
      ↓
   Use Tool
      ↓
Tool Result
      ↓
     Model
      ↓
Response to User
```

For example, if a user asks for the current weather, the assistant can use a weather tool to retrieve current information instead of relying only on what the model learned during training.

---

## 6. Agent

An **agent** is an AI system that can work toward a goal by deciding what steps to take, using available tools, observing the results, and continuing the workflow when necessary.

Instead of only answering a question, an agent can perform multiple steps toward achieving a goal.

A simplified agent workflow is:

```text
User Goal
    ↓
  Model
    ↓
Decide Next Step
    ↓
Use Tool / Retrieve Information
    ↓
Observe Result
    ↓
Decide Next Step
    ↓
Use Another Tool if Needed
    ↓
Final Result / Action
```

The important difference is that an agent can use a sequence of steps and tools to work toward a goal.

---

## 7. Simple Comparison

| System | Main Purpose | Uses External Information? | Uses Tools? | Can Perform Multi-Step Actions? |
|---|---|---|---|---|
| LLM | Generate and understand text | Not necessarily | No | No |
| AI Application | Provide an AI-powered software function | Depends on the application | Depends on the application | Depends on the application |
| RAG | Retrieve information and use it as context for generation | Yes | It can use a retrieval system | Usually limited to retrieval and generation |
| Tool-Using Assistant | Use external tools to obtain information or perform operations | Yes, when a tool provides it | Yes | Can perform multiple tool calls |
| Agent | Work toward a goal using reasoning, tools and multiple steps | Yes, when required | Yes | Yes |

This comparison shows that these terms describe different levels or capabilities of an AI system.

---

## 8. Simple Flow: User → Model → Tool/Retrieval → Result → Response/Action

A general tool-using AI workflow can be represented as:

```text
                 User
                   ↓
              User Request
                   ↓
                 Model
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
   Retrieval                Tool
        ↓                     ↓
   Information            Tool Result
        └──────────┬──────────┘
                   ↓
             Model processes
                the result
                   ↓
          ┌────────┴────────┐
          ↓                 ↓
       Response           Action
          ↓                 ↓
         User        External System
```

The important idea is that the model does not always have to produce the final answer directly.

It can first retrieve information or use a tool, process the result, and then provide a response or take an action.

---

## 9. Everyday Example of an Agentic Workflow

### Example: Planning and Booking a Trip

Consider a user who says:

> "Plan a weekend trip to Bengaluru for me, find a suitable hotel, and add the plans to my calendar."

An agentic system could break this goal into multiple steps.

A simplified workflow could be:

```text
User Goal
   ↓
Understand the trip requirements
   ↓
Search for suitable travel options
   ↓
Retrieve hotel information
   ↓
Compare available options
   ↓
Select an option based on the user's requirements
   ↓
Make the required booking or prepare the booking
   ↓
Add the itinerary to the calendar
   ↓
Confirm the completed actions
```

The system is not simply answering:

> "Here are some hotels in Bengaluru."

Instead, it can work through multiple steps toward the user's overall goal.

This illustrates the idea of an **agentic workflow**:

> **The system uses tools and multiple steps to move from a user's goal toward a result or action.**

---

## 10. Chatbot vs Agent

A traditional chatbot may work like this:

```text
User
 ↓
Question
 ↓
AI Model
 ↓
Answer
```

An agentic system can work more like this:

```text
User
 ↓
Goal
 ↓
AI Model
 ↓
Plan / Decide
 ↓
Use Tools
 ↓
Observe Results
 ↓
Decide Next Step
 ↓
Use More Tools if Needed
 ↓
Final Result / Action
```

Therefore, the main difference is not simply that one system uses AI and the other does not.

The important difference is the system's **ability to use information and tools and perform multiple steps toward a goal**.

---

## 11. Key Learning

From this mission, I learned that an LLM, an AI application, RAG, a tool-using assistant, and an agent are not exactly the same thing.

An LLM is the underlying language model.

An AI application uses AI as part of a larger software system.

RAG allows the system to retrieve external information and provide it to the model as context.

A tool-using assistant can interact with external tools.

An agent can use tools and multiple steps to work toward a goal.

The key idea I learned is:

> **A chatbot can answer a question, but a system becomes more agent-like when it can retrieve information, use tools, decide on steps, and take actions toward a goal.**

---

## 12. Important Distinction

An agent does not necessarily mean that the system is completely autonomous or can do anything by itself.

The available tools, permissions, instructions, and system design determine what actions it can actually perform.

Therefore, the word **agent** should be understood in terms of its ability to work through a goal using multiple steps and available tools, rather than simply assuming that every AI chatbot is an agent.

---

## 13. Final Reflection

The main difference I understood from this mission is the difference between **answering** and **acting toward a goal**.

A basic chatbot can generate an answer from the information available to it.

A RAG system can retrieve relevant information before generating an answer.

A tool-using assistant can interact with external tools.

An agent can combine these capabilities into a multi-step workflow to work toward a user's goal.

Therefore:

> **The more an AI system can retrieve information, use tools, make decisions about the next step, and carry out actions toward a goal, the more agentic the workflow becomes.**
