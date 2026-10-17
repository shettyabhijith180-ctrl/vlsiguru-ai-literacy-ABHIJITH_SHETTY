# Mission 4 — Understand ML Task Types

## 1. Introduction

Machine Learning (ML) can solve different kinds of problems depending on the required output. Before selecting a machine learning algorithm, it is important to understand the problem that needs to be solved.

The main ML task types covered in this mission are:

1. Classification
2. Regression
3. Clustering
4. Anomaly detection
5. Dimensionality reduction
6. Recommendation and ranking

Each task type has a different objective and produces a different kind of output.

For example, a model that predicts whether a VLSI design will pass or fail timing performs classification, whereas a model that estimates the critical-path delay performs regression.

Understanding the task type helps us identify the expected output and select a suitable approach for solving the problem.

---

## 2. Classification

### 2.1 Definition

Classification is a machine learning task in which a model predicts a category or class for an input.

The output belongs to a predefined set of categories. A classification problem may have two classes or multiple classes.

Examples include classifying an email as spam or not spam and predicting whether a VLSI design will pass or fail timing.

### 2.2 Input and Output

**Input:**
- Features describing the observation.
- Examples may include numerical measurements, categorical values, or other relevant information.

**Output:**
- A predicted category or class.

### 2.3 Simple Diagram

    Input Features
          |
          v
    Classification Model
          |
          v
    Predicted Category

### 2.4 VLSI Physical Design Example

Suppose historical Physical Design runs contain the following information:

- Standard-cell count
- Placement utilization
- Estimated congestion
- Estimated critical-path delay
- Final timing result

The final timing result is labelled as Pass or Fail.

A classification model could learn from historical design runs and predict whether a new design run is likely to pass or fail timing.

The input consists of relevant design features, and the output is the predicted timing category.

This prediction would need to be evaluated using unseen design runs before it could be trusted.

### 2.5 One Limitation

Classification depends on the quality of the training data and the class labels. If the training examples are insufficient or do not represent actual design conditions, the model may make incorrect predictions.

### 2.6 When Is It Suitable?

Classification is suitable when the required output is a category, such as Pass/Fail, defective/non-defective, or one of several predefined classes.

---

## 3. Regression

### 3.1 Definition

Regression is a machine learning task in which a model predicts a numerical value.

Unlike classification, which predicts categories, regression predicts quantities such as delay, temperature, power consumption, or manufacturing yield.

### 3.2 Input and Output

**Input:**
- Relevant features describing the observation.

**Output:**
- A predicted numerical value.

### 3.3 Simple Diagram

    Input Features
          |
          v
    Regression Model
          |
          v
    Predicted Numerical Value

### 3.4 VLSI Physical Design Example

Consider a Physical Design flow in which historical runs contain information about cell count, placement utilization, congestion, and other relevant design characteristics.

A regression model could use these features to estimate the critical-path delay of a new design run.

For example, the model might predict a critical-path delay of 850 ps.

The predicted delay could help engineers estimate timing performance before completing the entire implementation flow.

However, the prediction would not replace Static Timing Analysis (STA). Its usefulness would depend on the training data, prediction accuracy, and intended application.

### 3.5 One Limitation

Regression predictions may be inaccurate when the input differs significantly from the training data. The model may also perform poorly if the available features do not adequately explain the numerical outcome.

### 3.6 When Is It Suitable?

Regression is suitable when the objective is to estimate a numerical quantity, such as delay, power consumption, temperature, or yield.

---

## 4. Clustering

### 4.1 Definition

Clustering is a machine learning task that groups observations according to similarities in their characteristics.

It is commonly used when the data does not have supplied target labels for the grouping task.

Unlike classification, clustering does not necessarily begin with predefined categories. Instead, a clustering method identifies groups based on the selected features and similarity measure.

### 4.2 Input and Output

**Input:**
- A collection of observations.
- Relevant features describing each observation.

**Output:**
- Groups or clusters of similar observations.

### 4.3 Simple Diagram

    Unlabelled Data
          |
          v
    Clustering Method
          |
          v
    Groups of Similar Observations

### 4.4 VLSI Physical Design Example

Suppose an engineer has collected measurements from many Physical Design runs but does not have predefined categories for those runs.

The available features may include:

- Placement utilization
- Congestion measurements
- Standard-cell count
- Estimated delay

A clustering method could group design runs with similar characteristics.

For example, one cluster might contain runs with relatively high utilization and high congestion, while another might contain runs with lower utilization and lower congestion.

Engineers would then investigate the resulting groups to determine whether they reveal useful relationships or patterns.

A cluster should not automatically be interpreted as a timing failure or a timing success. The engineering meaning must be established through further analysis.

### 4.5 One Limitation

The resulting groups may not have an obvious engineering interpretation. Different feature selections or clustering methods may also produce different groupings.

### 4.6 When Is It Suitable?

Clustering is suitable when the objective is to explore data, identify groups of similar observations, or discover patterns without supplying predefined target labels.

---

## 5. Anomaly Detection

### 5.1 Definition

Anomaly detection is a machine learning task that identifies observations that differ significantly from expected or typical behaviour.

Anomalies may represent unusual measurements, unexpected operating conditions, defects, or potential failures.

An unusual observation is not necessarily an error. It may require further investigation to determine its cause.

### 5.2 Input and Output

**Input:**
- Measurements or features describing an observation.
- Reference data or a model of expected behaviour, depending on the method.

**Output:**
- An anomaly score, an anomaly flag, or a category indicating whether an observation is considered unusual.

### 5.3 Simple Diagram

    Input Measurements
            |
            v
    Anomaly Detection Model
            |
            v
    Anomaly Score or Flag
            |
            v
    Engineering Investigation

### 5.4 Semiconductor Manufacturing Example

Suppose a semiconductor manufacturing process produces measurements such as electrical test results, process parameters, and sensor readings.

An anomaly detection model could identify wafers or measurement records that differ significantly from typical observations.

Engineers could investigate these cases to determine whether they are associated with equipment problems, unusual process conditions, measurement errors, or genuine defects.

This example illustrates a potential application. An anomaly flag alone does not establish that a wafer is defective.

### 5.5 One Limitation

Anomaly detection may produce false alarms when normal variations are mistaken for unusual behaviour. It may also miss important failures if the abnormal patterns are not distinguishable using the available features.

### 5.6 When Is It Suitable?

Anomaly detection is suitable when the objective is to identify unusual observations, potential failures, or unexpected behaviour.

---

## 6. Dimensionality Reduction

### 6.1 Definition

Dimensionality reduction is a machine learning and data analysis task that represents data using fewer features or dimensions while attempting to preserve information relevant to the intended purpose.

Datasets may contain many features, some of which may be redundant or strongly correlated.

Reducing the number of dimensions can make data easier to visualise, analyse, or process.

### 6.2 Input and Output

**Input:**
- Data represented by many features or dimensions.

**Output:**
- A representation with fewer dimensions.

### 6.3 Simple Diagram

    High-Dimensional Data
             |
             v
    Dimensionality Reduction
             |
             v
    Lower-Dimensional Representation

### 6.4 Semiconductor Engineering Example

Suppose an engineer collects many measurements from semiconductor manufacturing, including electrical test parameters and process measurements.

A dataset containing hundreds of features may be difficult to visualise directly.

A dimensionality reduction method could transform the measurements into a smaller number of dimensions so that the main patterns can be explored more easily.

Engineers could then investigate whether the reduced representation reveals groups, trends, or unusual observations.

The reduced representation may not preserve every detail of the original data, so the suitability of the transformation must be evaluated.

### 6.5 One Limitation

Dimensionality reduction can discard information. The resulting dimensions may also be difficult to interpret in terms of the original engineering measurements.

### 6.6 When Is It Suitable?

Dimensionality reduction is suitable when a dataset has many features and the objective is to simplify its representation, support visualisation, or facilitate further analysis.

---

## 7. Recommendation and Ranking

### 7.1 Definition

Recommendation and ranking are related machine learning tasks used to suggest relevant items or arrange items according to their estimated relevance, usefulness, or preference.

**Recommendation** focuses on identifying items that may be useful to a user or application.

**Ranking** focuses on ordering candidate items according to a scoring criterion.

### 7.2 Input and Output

**Input:**
- Candidate items and their features.
- User preferences, interaction history, relevance information, or other context, depending on the application.

**Output:**
- A set of recommended items or an ordered list of ranked items.

### 7.3 Simple Diagram

    Candidate Items and Relevant Features
                    |
                    v
       Recommendation or Ranking Model
                    |
                    v
       Recommended or Ranked Items

### 7.4 Real-World Example

An online shopping platform may use a recommendation system to suggest products based on a user's previous interactions and preferences.

A search engine may use a ranking system to order results according to their estimated relevance to a query.

In these examples, the input includes information about candidate items and relevant context. The output is a recommendation or an ordered list.

### 7.5 One Limitation

Recommendations may be poor when interaction data is insufficient or does not represent a user's current interests. Ranking systems may also favour popular items and overlook less common but relevant choices.

### 7.6 When Is It Suitable?

Recommendation and ranking are suitable when the objective is to suggest useful items or order alternatives according to a defined relevance or preference criterion.

---

## 8. Comparison of ML Task Types

| Task Type | Main Objective | Typical Input | Expected Output | Example |
|---|---|---|---|---|
| Classification | Predict a category | Features describing a design run | Pass or Fail | Predict timing pass/fail |
| Regression | Predict a numerical value | Design features and measurements | Estimated delay in ps | Estimate critical-path delay |
| Clustering | Group similar observations | Unlabelled design measurements | Clusters of design runs | Group runs by congestion characteristics |
| Anomaly Detection | Identify unusual observations | Process measurements or design metrics | Anomaly score or flag | Identify unusual wafer measurements |
| Dimensionality Reduction | Represent data using fewer dimensions | Data containing many features | Lower-dimensional representation | Simplify manufacturing measurements for analysis |
| Recommendation and Ranking | Suggest or order relevant items | Candidate items and relevant context | Recommended items or ranked list | Rank search results by relevance |

The examples above are illustrative. The exact inputs and outputs depend on the problem being solved and the method selected.

---

## 9. Task Type Versus Learning Paradigm

A task type describes **what problem the model is intended to solve**, whereas a learning paradigm describes **how the model learns from available information or feedback**.

These concepts are related but are not interchangeable.

For example, classification is a task type. Supervised learning is a learning paradigm.

A supervised learning model can learn to classify historical examples when the correct class labels are available.

However, not every ML task uses the same learning paradigm.

### 9.1 Examples of the Difference

**Example 1: Classification**

A model learns from labelled design runs and predicts whether a new run will pass or fail timing.

- Task type: Classification
- Possible learning paradigm: Supervised learning

**Example 2: Clustering**

A model groups Physical Design runs based on similarities in their congestion measurements without using supplied group labels.

- Task type: Clustering
- Possible learning paradigm: Unsupervised learning

**Example 3: Anomaly Detection**

A model identifies unusual manufacturing measurements.

- Task type: Anomaly detection
- Possible learning paradigm: Unsupervised learning, supervised learning, or another suitable approach, depending on the available information and method.

**Example 4: Dimensionality Reduction**

A model transforms data containing many features into a smaller representation.

- Task type: Dimensionality reduction
- Possible approach: An unsupervised method or a self-supervised method, depending on the technique and training objective.

These examples show that a task type does not, by itself, specify how a model was trained.

### 9.2 Can Different Algorithms Solve the Same Task?

Yes. Different algorithms may solve the same task, although their suitability and performance can differ.

For example:

- Decision trees and logistic regression can both be used for classification.
- Linear regression and other regression methods can estimate numerical values.
- Different clustering algorithms can group similar observations.
- Different anomaly detection methods can identify unusual measurements.

The choice depends on the available data, the nature of the problem, computational requirements, interpretability, and evaluation results.

No single algorithm is automatically the best choice for every problem.

---

## 10. Key Learning

This mission helped me understand that machine learning can solve different types of problems, and each task has a specific objective and expected output.

Classification predicts categories, while regression predicts numerical values. Clustering identifies groups of similar observations, and anomaly detection identifies unusual observations. Dimensionality reduction simplifies the representation of data, whereas recommendation and ranking suggest or order relevant items.

In VLSI Physical Design, classification could be used to predict timing pass/fail, while regression could estimate critical-path delay. Clustering could help explore similarities among design runs, and dimensionality reduction could simplify large engineering datasets for analysis.

I also learned that task type and learning paradigm describe different aspects of a machine learning problem. The task type explains what the model needs to do, while the learning paradigm describes how it learns.

The final choice of a method should depend on the problem objective, available data, expected output, and evaluation requirements.

---

## 11. Sources and Further Reading

The following resources provide background on machine learning concepts and task types.

### Source 1 — Google: Introduction to Machine Learning

Link: https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

**What to verify:** The general definition of machine learning and the relationship between data, models, and predictions.

### Source 2 — Google: Machine Learning Crash Course

Link: https://developers.google.com/machine-learning/crash-course/

**What to verify:** Introductory ML concepts, including classification, regression, training data, and model evaluation.

### Source 3 — Scikit-learn: User Guide

Link: https://scikit-learn.org/stable/user_guide.html

**What to verify:** Examples and explanations of classification, regression, clustering, dimensionality reduction, and anomaly detection.

### Source Note

These resources provide general background on machine learning. The semiconductor examples in this mission are illustrative applications, not claims that a particular model has been demonstrated to improve a real VLSI Physical Design or semiconductor manufacturing flow.
