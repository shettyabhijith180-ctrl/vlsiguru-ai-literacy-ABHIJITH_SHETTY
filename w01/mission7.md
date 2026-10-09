# Mission 7 — What Actually Runs AI?

## 1. Introduction

AI models are software systems, but software cannot run without computing hardware.

When an AI application receives a prompt, the application uses a software framework to execute the model's computations on available hardware.

Depending on the system, the hardware may include a CPU, GPU, NPU, or another AI accelerator.

The main idea of this mission is to understand the relationship between AI software, computation, hardware, memory, and performance.

The basic mental model is:

```text
AI Model
   ↓
Computation
   ↓
Hardware
   ↓
Performance
```

## 2. What Is a CPU?

CPU stands for **Central Processing Unit**.

A CPU is a general-purpose processor designed to execute different types of instructions and handle a wide range of computing tasks.

Common CPU tasks include:

- Running the operating system.
- Executing application logic.
- Handling user input.
- Managing files and memory.
- Coordinating other hardware components.

A CPU is useful for tasks that require flexible instruction execution, complex control flow, and general-purpose computing.

For example, when a user opens an AI application, the CPU can handle the user interface, prepare the input, and coordinate the execution of the AI model.

## 3. What Is a GPU, and Why Is It Useful for AI?

GPU stands for **Graphics Processing Unit**.

GPUs were originally developed for graphics processing. They are also useful for AI because they can perform many similar mathematical operations in parallel.

AI models require large numbers of mathematical operations, including matrix multiplications.

A GPU can execute many of these operations simultaneously, making it suitable for many AI workloads.

For example, GPUs are widely used for training large neural networks and running AI models that require substantial computation.

A GPU does not replace every function of a CPU. The two processors often work together, with the CPU coordinating tasks and the GPU accelerating suitable computations.

## 4. What Is an NPU or AI Accelerator?

NPU stands for **Neural Processing Unit**.

An NPU is specialised hardware designed to accelerate neural-network and other AI-related computations.

An **AI accelerator** is a broader term for hardware designed to speed up AI workloads. An NPU is one type of AI accelerator.

Specialised hardware can be designed to execute common AI operations efficiently while reducing power consumption for suitable workloads.

Examples include:

- AI features on smartphones.
- Voice recognition.
- Image enhancement.
- Computer vision.
- Local AI assistants.

For example, a smartphone NPU can accelerate supported AI operations directly on the device without sending every computation to a cloud server.

## 5. What Does Parallel Computation Mean?

Parallel computation means performing multiple computations at the same time.

Consider a task that requires calculating several independent values.

A sequential approach processes the values one after another. A parallel approach processes multiple values simultaneously when the operations can be performed independently.

A simple illustration is:

```text
Sequential Computation

Task 1
  ↓
Task 2
  ↓
Task 3
  ↓
Task 4


Parallel Computation

Task 1 ─┐
Task 2 ─┤
Task 3 ─┼──→ Results
Task 4 ─┘
```

AI models contain many mathematical operations that can be parallelised.

This is one reason GPUs and AI accelerators are useful for AI workloads.

However, not every operation can be executed in parallel. Some operations depend on the results of earlier operations.

## 6. Why Does AI Depend on Compute and Memory?

AI models contain learned numerical parameters called **weights**.

Running an AI model requires mathematical computations using these parameters. The system must also store and move the data needed for those computations.

Two important requirements are computation and memory.

### 6.1 Compute

Compute refers to the hardware's ability to perform mathematical operations.

AI workloads may require a large number of operations, especially when the model contains many parameters or processes large inputs.

The available computing capability influences how quickly these operations can be completed.

### 6.2 Memory

Memory stores the information required during computation.

Examples include:

- Model weights.
- Input data.
- Intermediate computation results.
- Generated outputs.

The system must provide the required data to the processor.

If data cannot be supplied quickly enough, the processor may spend time waiting instead of performing useful computations.

Therefore, AI performance depends on both computational capability and memory capacity and bandwidth.

## 7. Training vs Inference

Training and inference are two different stages in the use of AI models.

### 7.1 Training

Training is the process through which a model learns from data by adjusting its parameters to improve its performance on a training objective.

A typical training process involves:

1. Providing training data to the model.
2. Performing forward computations.
3. Calculating a loss or error measure.
4. Computing gradients.
5. Updating the model parameters.
6. Repeating the process over training examples.

Training large models can require substantial computation, memory, and time.

### 7.2 Inference

Inference is the process of using a trained model to produce a prediction or response for new input.

For example, when a user asks an AI assistant a question, the model processes the input and generates a response. This is inference.

A typical inference process involves:

1. Receiving an input.
2. Processing the input using the trained model.
3. Performing the required computations.
4. Producing an output.

### 7.3 Main Difference

The main difference is:

- **Training:** Model parameters are adjusted through a learning process.
- **Inference:** The trained model uses its existing parameters to produce an output.

Both training and inference require computation and memory, but their computational requirements and patterns can differ.

## 8. How an AI Application Runs on Hardware

An AI application uses a model and supporting software to perform a task.

A software framework helps execute the model's operations on compatible hardware.

The following diagram shows a simplified view of the process:

```text
AI Application
      ↓
AI Model
      ↓
Software / Framework
      ↓
CPU / GPU / AI Accelerator
      ↕
    Memory
      ↓
Computation Results
      ↓
AI Application Output
```

The diagram is a simplified conceptual representation. Actual systems may use different execution paths, and memory can interact with the processor throughout computation.

The CPU may coordinate the application and other components. A GPU or AI accelerator may execute suitable model operations, while memory supplies the data and stores intermediate results.

The completed computations produce the output required by the AI application.

## 9. Real-World AI Workload: Image Recognition

### Example: Recognising Objects in an Image

Consider an AI application that identifies objects in a photograph.

The user uploads an image, and the application uses a trained neural network to identify objects such as cars, people, or buildings.

### Suitable Hardware

A **GPU** can be useful for this workload because image recognition models perform many mathematical operations that can be parallelised.

For a large image-recognition workload, a GPU can accelerate the model's computations.

An NPU may also be suitable when the model runs on a supported smartphone or other device with an appropriate AI accelerator.

The CPU can handle application logic, prepare the input, and coordinate execution.

### Simplified Workflow

```text
User Provides an Image
          ↓
AI Application
          ↓
Trained Image Recognition Model
          ↓
Software / Framework
          ↓
GPU or Suitable AI Accelerator
          ↕
        Memory
          ↓
Object Recognition Results
          ↓
Application Displays the Results
```

The most suitable hardware depends on factors such as model size, performance requirements, power consumption, memory capacity, and the hardware available in the system.

This example illustrates how AI software relies on computing hardware to perform the operations required to generate a result.

## 10. Key Learning

From this mission, I learned that an AI model is software, but running the model requires computation on hardware.

A CPU is a flexible general-purpose processor. A GPU is useful for workloads with many parallel operations, while an NPU or AI accelerator is specialised for suitable AI computations.

AI performance depends not only on computing capability but also on memory capacity and data movement.

I also learned the difference between training and inference. Training adjusts model parameters, whereas inference uses the trained model to produce outputs.

The key idea is:

> AI software defines the computations, computing hardware executes them, and the available compute and memory resources influence performance.
