# Mission 2 — Understand Data: What Does an ML System Learn From?

## 1. Introduction

Machine Learning (ML) systems learn patterns from data and use those patterns to make predictions or identify relationships in new examples. The quality and suitability of the data strongly influence how useful these predictions can be.

For example, in VLSI Physical Design, an ML model could learn from historical design-run data to estimate whether a new design is likely to pass timing. The data might include cell count, placement utilization, congestion measurements, and the known timing outcome.

Before understanding how a model learns, it is important to understand datasets, samples, observations, features, labels, and targets.

The dataset used in this mission is a **synthetic illustrative example**. Its values are created for learning purposes and are not actual measurements from an industrial design flow.

---

## 2. Basic Data Concepts

### 2.1 Dataset

A dataset is a collection of related data samples or observations used for analysis or machine learning.

For example, a collection of historical VLSI design runs containing cell counts, utilization percentages, congestion measurements, and timing outcomes is a dataset.

### 2.2 Sample

A sample is one example in a dataset.

For example, the measurements and timing outcome associated with one physical design run form a sample.

### 2.3 Observation

An observation is one recorded instance of the system or event being studied.

In the VLSI example, one row representing a particular design run is an observation. In this dataset, the terms sample and observation refer to the same individual design run.

### 2.4 Feature

A feature is an input variable that describes a sample and may help a model make a prediction.

Possible features in a VLSI design dataset include:

- Standard-cell count
- Placement utilization
- Estimated congestion
- Estimated critical-path delay

A model may examine these features to identify patterns associated with timing outcomes.

### 2.5 Label

A label is the known answer or outcome associated with an example, particularly in supervised learning.

For example, a completed design run may have a label indicating whether it passed or failed timing.

Labels provide the reference answers from which a supervised model can learn.

### 2.6 Target

The target is the specific outcome a model is intended to predict.

In this example, the target is `Timing_Outcome`, which has two possible values: `Pass` and `Fail`.

The target is also the label in this supervised classification example.

**In simple terms:**
- Dataset: The complete collection of examples.
- Sample or observation: One example in the dataset.
- Feature: Information used as input.
- Label: The known answer associated with an example.
- Target: The outcome the model is designed to predict.

---

## 3. Types of Data

### 3.1 Structured Data

Structured data is organised in a predefined format, commonly using rows and columns.

For example, a spreadsheet containing design-run IDs, cell counts, utilization percentages, and timing outcomes is structured data.

Structured data is generally easier to organise, filter, compare, and analyse using conventional data-processing tools.

### 3.2 Unstructured Data

Unstructured data does not follow a simple, predefined tabular structure.

Examples include:

- Design review notes written in natural language.
- Images of semiconductor defects.
- Free-form engineering reports.
- Screenshots of timing reports.

Unstructured data may require additional processing before it can be used effectively in an ML system.

Some engineering data, such as timing reports and log files, may contain both structured and unstructured information.

### 3.3 Numerical Features

Numerical features represent quantities using numbers.

Examples include:

- Cell count: 12,000
- Placement utilization: 65%
- Estimated congestion: 18%
- Estimated critical-path delay: 850 ps

Numerical features can represent counts, measurements, or other quantities. Their meaning and units must be understood before analysis.

### 3.4 Categorical Features

Categorical features represent groups or categories rather than measured quantities.

Examples include:

- Design block type: Datapath, Memory Interface, or Control Logic.
- Process corner: A specified process-voltage-temperature corner.
- Timing outcome: Pass or Fail.

Although categories may sometimes be represented using numbers in a computer system, those numbers do not necessarily represent numerical quantities.

For example, assigning the values 1, 2, and 3 to three block types does not mean that block type 3 is numerically greater than block type 1.

### 3.5 Labelled and Unlabelled Data

**Labelled data** contains examples with known outcomes or labels.

For example, a dataset containing design measurements and the corresponding Pass or Fail timing result is labelled data.

**Unlabelled data** contains input information without the outcome labels required for a particular supervised prediction task.

For example, a collection of design-run measurements without known timing outcomes is unlabelled for the task of predicting timing pass or fail.

Labelled data can be used to train supervised ML models. Unlabelled data can be useful for exploring patterns or grouping similar observations using appropriate methods.

---

## 4. Illustrative Dataset: Predicting Timing Pass or Fail

### 4.1 Problem Statement

The objective is to explore whether historical design measurements could help predict if a new VLSI Physical Design run will pass timing.

The dataset contains eight synthetic design-run observations.

The measurements and outcomes below are illustrative only. They are not actual industrial data, and the values have not been validated to represent a real design flow.

### 4.2 Dataset

| Run ID | Cell Count | Placement Utilization (%) | Estimated Congestion (%) | Estimated Critical-Path Delay (ps) | Timing Outcome |
|---|---:|---:|---:|---:|---|
| RUN_01 | 8000 | 55 | 12 | 780 | Pass |
| RUN_02 | 10000 | 60 | 15 | 820 | Pass |
| RUN_03 | 12000 | 65 | 18 | 850 | Pass |
| RUN_04 | 14000 | 72 | 25 | 930 | Fail |
| RUN_05 | 16000 | 78 | 32 | 980 | Fail |
| RUN_06 | 9000 | 58 | 14 | 800 | Pass |
| RUN_07 | 15000 | 75 | 29 | 960 | Fail |
| RUN_08 | 11000 | 68 | 21 | 890 | Pass |

**Note:** These synthetic values are designed to illustrate the data concepts. They should not be interpreted as evidence that any particular utilization, congestion, or delay value guarantees a timing outcome.

### 4.3 Identifying the Features and Target

The features are the input measurements that could be used to make a prediction.

In this dataset, the features are:

1. Cell Count
2. Placement Utilization (%)
3. Estimated Congestion (%)
4. Estimated Critical-Path Delay (ps)

The target is:

- `Timing Outcome`

The target contains two categories: `Pass` and `Fail`.

`Run ID` is an identifier used to distinguish observations. It is not intended to be a predictive feature in this example.

Because the target is a known category, this is an example of a potential supervised classification problem.

In a real project, engineers would need to confirm that the input measurements are available at the intended prediction stage. For example, a final timing result should not be used as an input when the goal is to predict that same result before it is known.

### 4.4 Data Type Classification

| Column | Data Type | Role |
|---|---|---|
| Run ID | Identifier / categorical text | Identifies each observation |
| Cell Count | Numerical | Feature |
| Placement Utilization (%) | Numerical | Feature |
| Estimated Congestion (%) | Numerical | Feature |
| Estimated Critical-Path Delay (ps) | Numerical | Feature |
| Timing Outcome | Categorical | Target / label |

The dataset is structured because its information is organised into rows and columns.

It is labelled because the known timing outcome is provided for each observation.

---

## 5. Data Collection and Data Cleaning

### 5.1 Data Collection

Data collection is the process of gathering relevant information for a particular problem.

In a real VLSI Physical Design project, potential data sources could include:

- Placement and routing reports.
- Congestion reports.
- Timing reports.
- Design configuration information.
- Historical design-run outcomes.

The data should be relevant to the problem being investigated. Engineers should also verify that the measurements are collected consistently and that their definitions are understood.

### 5.2 Data Cleaning

Data cleaning involves identifying and handling problems that could make a dataset unreliable.

Common data-quality problems include the following.

**Missing values:** Some observations may not contain all the required measurements.

**Noisy data:** Measurements may contain errors or unexpected variations caused by measurement processes, tool behaviour, or other factors.

**Inconsistent labels:** Different records may assign different outcomes to equivalent cases because of incorrect reporting or inconsistent definitions.

**Inconsistent formats:** Measurements may use different units or formats. For example, one report may record delay in picoseconds while another records it in nanoseconds.

Before using data, engineers should investigate these problems and apply suitable corrections or document the limitations.

Cleaning should not mean removing inconvenient observations simply because they do not match expectations. The reasons for any changes should be understood and documented.

---

## 6. Why Data Quantity Alone Does Not Guarantee Data Quality

Having a large dataset does not automatically make an ML model reliable.

A dataset may contain thousands of observations but still be unsuitable if its measurements are incorrect, important cases are missing, or labels are inconsistent.

For example, a model trained on a large collection of design runs from only one narrow set of design conditions may perform poorly when applied to a different type of design.

Similarly, a large dataset with incorrectly recorded timing outcomes may teach the model misleading relationships.

Useful data should be relevant to the problem, sufficiently representative of the situations in which the model will be used, consistently measured, and correctly labelled where labels are required.

Therefore, both the quantity and the quality of the data matter.

---

## 7. Two Ways Data Quality Can Affect an ML Model

### 7.1 Missing or Incorrect Measurements

Suppose several design runs have missing congestion measurements, or some congestion values were recorded incorrectly.

The model may fail to learn the relationship between congestion and timing outcomes accurately. Depending on how the problem is handled, the missing or incorrect values may also introduce bias into the data.

**Possible impact:** Predictions may become less reliable, especially for design runs with characteristics that were poorly represented in the training data.

**Possible mitigation:** Investigate the source of the problem, verify measurements against original reports where possible, and use an appropriate method to handle missing or incorrect values. The chosen method should be documented.

### 7.2 Incorrect or Inconsistent Timing Labels

Suppose a design run that failed the required timing checks is incorrectly recorded as `Pass`.

The model may learn from an incorrect example. If many labels are wrong, the model may learn misleading patterns between the input measurements and the timing outcome.

**Possible impact:** The model could incorrectly predict that a design will pass timing when it is actually likely to fail.

**Possible mitigation:** Verify labels against the relevant timing reports and apply a consistent definition of timing pass or fail across the dataset.

These examples demonstrate that even an ML method that is suitable for the problem can produce unreliable results when its data is poor.

---

## 8. Key Learning

This mission helped me understand that an ML system learns patterns from examples, so the structure and reliability of the data are important.

A dataset contains observations, and each observation contains information represented by features. In supervised learning, labelled examples also provide known outcomes. The target is the outcome that the model is intended to predict.

Data can be structured or unstructured, and features can be numerical or categorical. Data can also be labelled or unlabelled, depending on whether the relevant outcomes are available.

In VLSI Physical Design, historical measurements could potentially be used to predict timing outcomes. However, the usefulness of such a model would depend on the accuracy, consistency, and representativeness of the data, as well as proper evaluation.

I also learned that a large dataset is not necessarily a good dataset. Missing measurements, noisy values, and incorrect labels can cause a model to learn misleading patterns and produce unreliable predictions.

---

## 9. Sources and Further Reading

The following resources are relevant to the concepts covered in this mission. Consult the pages and retain the sources you actually use when finalising this assignment.

### Source 1 — Google: Introduction to Machine Learning

Link: https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

**What to verify:** The basic definition of machine learning and the distinction between conventional programming and learning from examples.

### Source 2 — Google: Machine Learning Crash Course

Link: https://developers.google.com/machine-learning/crash-course

**What to verify:** The introductory explanations of datasets, numerical data, categorical data, and the role of data in machine learning.

### Source 3 — IBM: What Is Machine Learning?

Link: https://www.ibm.com/think/topics/machine-learning

**What to verify:** The general role of data in machine learning and how trained models use learned patterns to make predictions.

The dataset in this mission is synthetic and was created to illustrate the concepts. The sources above are for understanding the general ML concepts; they are not evidence that the example dataset represents actual semiconductor design behaviour.
