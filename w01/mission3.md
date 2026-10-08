# Mission 3 — Is it really AI?

## 1. Classification Table

| Example | Classification | Reason |
|---|---|---|
| Calculator | Rule-based / Traditional software | A calculator performs explicitly programmed mathematical operations and does not learn from data. |
| Temperature warning rule | Rule-based / Traditional software | It follows a predefined condition, such as giving a warning when the temperature exceeds a fixed threshold. |
| Spam filter | ML-based AI | A modern spam filter can learn patterns from examples of spam and normal messages and use those patterns to classify new messages. |
| Document summariser | Generative AI | A modern AI summariser can use a generative model to produce a shorter version of a document. |
| Traffic ETA prediction | ML-based AI | A machine-learning model can learn from traffic data and use the learned patterns to predict travel time. |

---

## 2. An Easy Classification

### Temperature Warning Rule

The temperature warning rule was easy to classify because its behaviour is explicitly defined by a condition.

For example:

```text
IF temperature > 50°C
        ↓
   Give warning
```

The system does not learn from previous temperature measurements. It simply follows a rule written by a programmer or system designer.

Therefore, it is mainly **rule-based/traditional software**.

---

## 3. A Difficult Classification

### Spam Filter

The spam filter was more difficult to classify because a spam filter can be implemented using either predefined rules or machine learning.

For example, a simple rule-based system could classify an email as spam if it contains a particular word or pattern.

```text
IF message contains a specific spam pattern
        ↓
       Spam
```

On the other hand, a machine-learning spam filter can be trained using examples of spam and normal messages. The model learns patterns from these examples and uses them to classify new messages.

Therefore, for this mission, I classify a modern spam filter as **ML-based AI**, while recognising that some spam filters can also be rule-based.

---

## 4. My Own Example

### Automatic Fan Controller

An automatic fan controller can use a predefined temperature rule.

For example:

```text
IF temperature > 30°C
        ↓
    Fan ON

IF temperature < 28°C
        ↓
    Fan OFF
```

The behaviour is explicitly defined by rules, and the system does not learn patterns from data.

Therefore, this is mainly **rule-based/traditional software**, not machine-learning AI.

---

## 5. Key Learning

The important lesson from this mission is that a system behaving intelligently does not automatically mean that it is using AI.

A rule-based system follows explicitly written instructions:

```text
Human-written rules
        ↓
Program follows rules
        ↓
      Output
```

A machine-learning system instead learns patterns from data:

```text
Training data
      ↓
ML algorithm
      ↓
Learned model
      ↓
New input
      ↓
Prediction
```

Therefore, **explicitly written rules are not the same as a model learning patterns from data**.
