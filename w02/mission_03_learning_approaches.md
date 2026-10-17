# Mission 3 — Understand the Main ML Approaches

## 1. Introduction

Machine Learning (ML) systems can learn in different ways depending on the information available during training and the feedback they receive.

The three main learning approaches covered in this mission are:

1. Supervised learning
2. Unsupervised learning
3. Reinforcement learning

Self-supervised learning is another related approach in which training targets are derived from the data itself.

Understanding these approaches helps us determine which type of learning may be suitable for a particular engineering problem.

For example, in VLSI Physical Design, historical design data with known timing outcomes could be used for supervised learning, while design data without known outcomes could be explored using unsupervised learning.

---

## 2. Supervised Learning

### 2.1 Definition

Supervised learning is an ML approach in which a model learns from labelled training examples. Each example contains input information and a known target or correct answer.

The model learns relationships between the inputs and their corresponding targets. After training, it can use these learned relationships to make predictions for new examples.

### 2.2 Training Signal

The training signal consists of the known labels or target values associated with the training examples.

The model's predictions are compared with the expected targets, and a learning algorithm adjusts the model to reduce prediction errors.

### 2.3 Simple Diagram

```text
        Labelled Training Data
       (Inputs + Known Targets)
                  |
                  v
            Learning Algorithm
                  |
                  v
             Trained Model
                  |
                  v
          New, Unseen Input Data
                  |
                  v
             Prediction
```

### 2.4 VLSI Physical Design Example

Suppose we have historical Physical Design runs containing:

- Standard-cell count
- Placement utilization
- Estimated congestion
- Estimated critical-path delay
- Final timing outcome

The final timing outcome is labelled as `Pass` or `Fail`.

A supervised learning model could learn from these historical examples and predict whether a new design run is likely to pass or fail timing.

This is a potential **classification problem** because the target contains categories.

The usefulness of the model would depend on data quality, representative training examples, and evaluation on unseen design runs.

### 2.5 What Does It Produce?

Depending on the problem, supervised learning can produce:

- A predicted category, such as `Pass` or `Fail`.
- A predicted numerical value, such as an estimated delay.

Classification predicts categories, while regression predicts numerical values.

### 2.6 One Limitation

Supervised learning requires suitable labelled examples for the intended prediction task. Incorrect labels, insufficient examples, or data that does not represent real operating conditions can lead to unreliable predictions.

### 2.7 When Is It Suitable?

Supervised learning is suitable when:

- Historical examples are available.
- The relevant outcomes or target values are known.
- The objective is to predict an outcome for new examples.

---

## 3. Unsupervised Learning

### 3.1 Definition

Unsupervised learning is an ML approach in which a model works with data that does not have supplied target labels for the task being performed.

Instead of learning from known answers, the model attempts to identify patterns, similarities, groupings, or other structures in the data.

### 3.2 Training Signal

The model uses the structure and characteristics of the input data rather than supplied target labels.

The specific method determines how patterns or relationships are identified.

### 3.3 Simple Diagram

```text
          Unlabelled Data
                  |
                  v
          Learning Algorithm
                  |
                  v
       Patterns or Groups Identified
                  |
                  v
       Interpretation of the Results
```

### 3.4 VLSI Physical Design Example

Suppose an engineer has measurements from many Physical Design runs but does not have timing outcome labels for the task being investigated.

The available data may include:

- Standard-cell count
- Placement utilization
- Congestion measurements
- Estimated delay

An unsupervised learning method, such as clustering, could group design runs with similar characteristics.

For example, the groups might contain runs with similar utilization and congestion measurements.

The groups would need to be analysed before assigning them an engineering interpretation. A cluster should not automatically be assumed to represent a timing failure or a timing success.

### 3.5 What Does It Produce?

Depending on the method, unsupervised learning can produce:

- Groups of similar observations.
- Patterns or relationships in the data.
- Lower-dimensional representations of the data.

### 3.6 One Limitation

The discovered groups or patterns may not have an obvious engineering meaning. The results may require domain knowledge and further investigation before they can support decisions.

### 3.7 When Is It Suitable?

Unsupervised learning is suitable when:

- The available data does not have supplied target labels for the task.
- The objective is to explore the data.
- The engineer wants to identify groups, patterns, or unusual observations.

---

## 4. Reinforcement Learning

### 4.1 Definition

Reinforcement learning is an ML approach in which an agent learns by interacting with an environment.

The agent takes actions and receives feedback in the form of rewards or penalties. Over time, it learns a strategy, often called a policy, intended to maximise cumulative reward.

Unlike conventional supervised learning, the agent does not simply learn from a dataset of input examples paired with correct answers for every action.

### 4.2 Training Signal

The training signal includes rewards or penalties received after the agent takes actions and observes the consequences.

The reward design is important because the agent's behaviour is influenced by what the reward encourages.

### 4.3 Simple Diagram

```text
             Environment
                  |
                  v
        State or Observation
                  |
                  v
                 Agent
                  |
                  v
                Action
                  |
                  v
             Environment
                  |
                  v
          Reward and New State
                  |
                  v
            Learning Continues
```

### 4.4 VLSI Physical Design Example

Consider a hypothetical research system intended to explore placement optimisation.

An agent could select an action that changes a placement-related setting or makes a permitted optimisation move. The environment could then evaluate the resulting design and provide feedback based on a defined objective.

For example, a reward function might consider improvements in timing while penalising excessive area or power.

The exact reward function would need to reflect the engineering objectives and constraints. The system would also need a suitable environment in which actions and their consequences can be evaluated.

This is an illustrative application, not a claim that reinforcement learning is automatically better than conventional optimisation methods.

### 4.5 What Does It Produce?

Reinforcement learning can produce a policy or strategy that selects actions based on the current state or observation.

The objective is to learn behaviour that maximises cumulative reward according to the defined problem.

### 4.6 One Limitation

Designing a useful reward function can be difficult. A poorly designed reward may encourage behaviour that improves the reward score without satisfying the actual engineering requirements.

Training can also require substantial interaction with the environment and careful management of constraints.

### 4.7 When Is It Suitable?

Reinforcement learning may be suitable when:

- The problem involves a sequence of decisions or actions.
- Actions affect later states or outcomes.
- Feedback can be provided through rewards or penalties.
- The environment can be evaluated safely and meaningfully.

---

## 5. Comparison of the Three Main Learning Approaches

| Aspect | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|---|---|---|---|
| Main idea | Learn from examples with known targets | Identify patterns or structure in data | Learn through actions and feedback |
| Training signal | Known labels or target values | Structure of the input data | Rewards or penalties |
| Required information | Input examples and corresponding targets | Input data without supplied task labels | States or observations, actions, and rewards |
| Typical output | Predicted category or numerical value | Groups, patterns, or representations | A policy or strategy for selecting actions |
| Example method | Classification or regression | Clustering | Learning a policy through interaction |
| VLSI example | Predict timing Pass/Fail from labelled design runs | Group design runs with similar congestion characteristics | Explore placement-related actions using a defined reward |
| One limitation | Requires suitable labelled examples | Discovered patterns may be difficult to interpret | Reward design and environment interaction can be challenging |
| Suitable when | Known outcomes are available for prediction | Exploring patterns in data is the goal | Learning a sequence of decisions is the goal |

**Important distinction:** These approaches describe how learning takes place. The type of problem being solved, such as classification or clustering, is a separate concept that will be discussed in the next mission.

---

## 6. Self-Supervised Learning

### 6.1 Definition

Self-supervised learning is an approach in which training targets are generated from the data itself rather than being supplied as manually assigned labels for every example.

A learning system creates a training task from the available data and learns by predicting or reconstructing the derived targets.

Self-supervised learning is commonly used to learn useful representations from large amounts of data.

### 6.2 Simple Diagram

```text
              Raw Data
                  |
                  v
        Create a Training Task
        from the Data Itself
                  |
                  v
       Input and Derived Target
                  |
                  v
          Learning Algorithm
                  |
                  v
       Model Learns Representations
```

### 6.3 Example

Consider a collection of engineering reports.

A self-supervised training task could hide selected words from a report and train a model to predict the missing words using the surrounding text.

The original text provides the information needed to construct the training targets, so manually labelling every missing word is unnecessary.

This is a simplified illustration of a self-supervised learning task.

### 6.4 How Is It Different from Unsupervised Learning?

Both approaches can work without manually supplied labels for the original data. However, they are not always interchangeable terms.

In self-supervised learning, a training signal is explicitly constructed from the data itself. The model learns by solving the derived prediction or reconstruction task.

In unsupervised learning, the broader objective is to identify patterns or structure without supplied target labels for the task.

Self-supervised methods are often discussed as a distinct learning approach because of the way their training targets are constructed, even though they are closely related to learning from unlabelled data.

### 6.5 Connection to Deep Learning

Self-supervised learning is important in modern deep learning because it can use large amounts of raw text, images, audio, or other data to learn useful representations.

For example, some language models are trained using tasks in which parts of the text are predicted from other parts of the text.

The details of neural networks and large language models will be explored later in the coursework.

---

## 7. Key Differences: What Signal Does Each Approach Use?

The most important difference among these learning approaches is the source of the training signal.

- **Supervised learning:** Learns from examples with known target labels or values.
- **Unsupervised learning:** Searches for patterns or structure in data without supplied target labels for the task.
- **Reinforcement learning:** Learns from the consequences of actions and the rewards or penalties received.
- **Self-supervised learning:** Constructs training targets from the data itself.

The approaches should be selected according to the problem, available information, desired output, and evaluation requirements.

---

## 8. Key Learning

This mission helped me understand that ML systems can learn in different ways depending on the training information and feedback available.

Supervised learning is useful when historical examples have known outcomes. In VLSI Physical Design, this could support a model that predicts a timing outcome from suitable historical design data.

Unsupervised learning is useful for exploring data and identifying groups or patterns when target labels are not supplied for the task.

Reinforcement learning focuses on learning a strategy through actions and reward feedback. It may be relevant to sequential optimisation problems, provided that the environment and reward function are designed appropriately.

Self-supervised learning derives its training targets from the data itself. It is related to unsupervised learning but is often distinguished by the explicit training task constructed from the data.

I also learned that no learning approach is automatically suitable for every problem. The choice depends on the objective, available data, feedback mechanism, and limitations of the approach.

---

## 9. Sources and Further Reading

The following resources can be consulted to verify the concepts discussed in this mission.

### Source 1 — Google: Introduction to Machine Learning

Link: https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

**What to verify:** The general definition of machine learning, learning from examples, and the distinction between different ML approaches.

### Source 2 — Google: Machine Learning Crash Course

Link: https://developers.google.com/machine-learning/crash-course

**What to verify:** Introductory ML concepts, including training data, labels, models, and supervised learning.

### Source 3 — IBM: What Is Machine Learning?

Link: https://www.ibm.com/think/topics/machine-learning

**What to verify:** The role of data in machine learning and the general distinction between ML approaches.

### Source 4 — OpenAI: Language Models and Self-Supervised Learning

Link: https://openai.com/research/

**What to verify:** Background research on modern language models and related learning methods. Consult a specific relevant publication before using it to support a particular technical claim.

**Note:** These sources provide background on ML concepts. They do not establish that any particular ML approach will improve a real VLSI Physical Design flow. Such a claim would require evidence from an appropriate engineering study.
