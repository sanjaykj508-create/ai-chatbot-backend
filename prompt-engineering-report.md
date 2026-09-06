# Prompt Engineering: Few-Shot, Reasoning, and Structured Output

## 1. Objective

The objective of this task was to gain practical experience with three prompt-engineering techniques:

1. Zero-shot vs. few-shot prompting
2. Step-by-step reasoning
3. Structured JSON output

The experiments were performed using Google AI Studio with a Gemini model.

---

# 2. Experiment 1 — Zero-Shot vs. Few-Shot Prompting

## Task

The task was to classify sentences as Positive, Negative, or Neutral.

Five test sentences were used.

## 2.1 Zero-Shot Prompt

```text
Classify each sentence as Positive, Negative, or Neutral.

Return the answers in order, using only the labels.

1. "The delivery was incredibly fast and the product quality is excellent."
2. "I waited two hours for my order and the food arrived cold."
3. "The package contains a black notebook and two pens."
4. "The customer service team was extremely helpful and friendly."
5. "The software keeps crashing and I am very disappointed."
```

### Raw Model Output

```text
1. Positive
2. Negative
3. Neutral
4. Positive
5. Negative
```

## 2.2 Few-Shot Prompt

```text
Classify the sentiment of each sentence as Positive, Negative, or Neutral.

Examples:

Sentence: "I absolutely loved the movie."
Sentiment: Positive

Sentence: "The food was cold and tasteless."
Sentiment: Negative

Sentence: "The meeting is scheduled for 3 PM."
Sentiment: Neutral

Now classify the following sentences:

1. "The delivery was incredibly fast and the product quality is excellent."
2. "I waited two hours for my order and the food arrived cold."
3. "The package contains a black notebook and two pens."
4. "The customer service team was extremely helpful and friendly."
5. "The software keeps crashing and I am very disappointed."

Return the answers in order, using only the labels.
```

### Raw Model Output

```text
1. Positive
2. Negative
3. Neutral
4. Positive
5. Negative
```

## Results

| Method | Correct | Accuracy |
|---|---:|---:|
| Zero-shot | 5/5 | 100% |
| Few-shot | 5/5 | 100% |

## Analysis

Both zero-shot and few-shot prompting produced the correct classification for all five test inputs. Few-shot prompting did not improve accuracy on this simple dataset.

However, the examples clearly demonstrated how the sentiment labels should be interpreted. This can be useful for more ambiguous tasks or when a specific output format is required.

---

# 3. Experiment 2 — Step-by-Step Reasoning

## Task

A multi-step mathematical problem was used to compare a direct prompt with a step-by-step prompt.

### Problem

A shop gives a 20% discount on a shirt that costs ₹1,500. After the discount, a customer pays an additional 5% tax on the discounted price. What is the final amount the customer pays?

## 3.1 Direct Prompt

```text
A shop gives a 20% discount on a shirt that costs ₹1,500. After the discount, a customer pays an additional 5% tax on the discounted price. What is the final amount the customer pays?

Give only the final answer.
```

### Raw Model Output

```text
1260
```

## 3.2 Step-by-Step Prompt

```text
Solve this problem carefully.

A shop gives a 20% discount on a shirt that costs ₹1,500. After the discount, a customer pays an additional 5% tax on the discounted price. What is the final amount the customer pays?

Explain the calculation briefly, then give the final answer.
```

### Raw Model Output

The model gave the correct answer of ₹1,260 with clear calculation steps.

## Results

| Prompt | Result |
|---|---|
| Direct prompt | ₹1,260 — Correct |
| Step-by-step prompt | ₹1,260 — Correct |

## Analysis

Both prompts produced the correct final answer. The direct prompt was sufficient for this problem, while the step-by-step prompt made the intermediate calculations easier to understand and verify.

Therefore, step-by-step prompting improved clarity but did not improve final accuracy in this particular test.

---

# 4. Experiment 3 — Structured JSON Output

## Task

The goal was to extract a person's name, date, and payment amount from text.

The required structure was:

```json
{
  "name": "person's name",
  "date": "YYYY-MM-DD",
  "amount": 0
}
```

## 4.1 Initial Prompt Test

### Input

"Yesterday, Sanjay purchased a Python course for ₹1,500. The payment was made on September 5, 2026."

### Raw Model Output

```json
{
  "name": "Python course",
  "date": "September 5, 2026",
  "amount": 1500
}
```

### Result

Failed because the model incorrectly identified "Python course" as the person's name.

---

## 4.2 Improved Prompt

```text
Extract information from the text.

Rules:
1. "name" must contain the PERSON'S NAME, not a product, course, or company.
2. "date" must use YYYY-MM-DD format.
3. "amount" must be a number without currency symbols.
4. Return ONLY valid JSON.
5. Follow this exact schema:

{
  "name": "string",
  "date": "YYYY-MM-DD",
  "amount": 0
}
```

## Test 1

### Input

"Yesterday, Sanjay purchased a Python course for ₹1,500. The payment was made on September 5, 2026."

### Raw Output

```json
{
  "name": "Sanjay",
  "date": "2026-09-05",
  "amount": 1500
}
```

Result: PASS

## Test 2

### Input

"Priya bought a laptop bag for ₹2,499. She completed the payment on August 20, 2026."

### Raw Output

```json
{
  "name": "Priya",
  "date": "2026-08-20",
  "amount": 2499
}
```

Result: PASS

## Test 3

### Input

"On July 15, 2026, Arjun paid ₹850 for an online Python workshop."

### Raw Output

```json
{
  "name": "Arjun",
  "date": "2026-07-15",
  "amount": 850
}
```

Result: PASS

## Test 4

### Input

"Meena registered for a data analytics course costing ₹3,200 on June 10, 2026."

### Raw Output

```json
{
  "name": "Meena",
  "date": "2026-06-10",
  "amount": 3200
}
```

Result: PASS

## Test 5

### Input

"Rahul purchased a programming book for ₹750 on May 25, 2026."

### Raw Output

```json
{
  "name": "Rahul",
  "date": "2026-05-25",
  "amount": 750
}
```

Result: PASS

## Results

| Test | Result |
|---|---|
| Test 1 | PASS |
| Test 2 | PASS |
| Test 3 | PASS |
| Test 4 | PASS |
| Test 5 | PASS |
| Total | 5/5 |
| Success Rate | 100% |

## Analysis

The initial prompt failed because the meaning of the "name" field was ambiguous. The model selected "Python course" instead of the person's name.

The improved prompt clearly defined each field, specified the date format, required the amount to be a number, and instructed the model to return only JSON. These changes improved reliability and resulted in a 100% success rate across the five final tests.

---

# 5. Overall Results

| Technique | Result | Main Finding |
|---|---|---|
| Zero-shot | 5/5 — 100% | Worked well for simple sentiment classification |
| Few-shot | 5/5 — 100% | Did not improve accuracy on this dataset |
| Direct reasoning | Correct | Produced the correct answer |
| Step-by-step reasoning | Correct | Improved explanation clarity |
| Initial JSON prompt | Failed | Ambiguous field definition |
| Improved JSON prompt | 5/5 — 100% | Explicit schema improved reliability |

---

# 6. Key Lessons Learned

### Few-Shot Prompting

Examples help demonstrate expected behavior and output format. However, few-shot prompting does not automatically improve accuracy when the task is already simple.

### Step-by-Step Reasoning

Step-by-step instructions can make multi-step calculations easier to understand and verify. In this experiment, they improved clarity but did not change the final answer.

### Structured Output

Explicit schemas and clear field definitions are useful when reliable machine-readable output is required. The improved prompt achieved a 100% success rate across five structured-output tests.

---

# 7. Conclusion

This hands-on experiment demonstrated that prompt design affects the reliability and usefulness of LLM outputs.

The experiments showed that more prompting is not always better. Zero-shot prompting already achieved 100% accuracy on the sentiment dataset, and step-by-step prompting did not change the mathematical answer. In contrast, structured-output prompting showed a clear improvement after the fields and formatting requirements were explicitly defined.

The main lesson learned is that effective prompt engineering involves matching the prompting technique to the task, testing the results, recording failures honestly, and improving the prompt based on those failures.

**Final takeaway:** Reliable LLM behavior comes from clear instructions, useful examples, explicit output formats, and systematic testing.
