# 🧠 What They Typically Test

## 1. Algorithmic Thinking (Yes, even for DevOps)

Even for SRE/DevOps, Codility often includes **coding problems** to test how you think.

Expect:

* Arrays, strings (e.g. binary gap, rotations, parsing logs)
* Basic data structures (sets, dicts, stacks)
* Time/space complexity awareness

👉 Example types:

* Log parsing (very common for SRE)
* Finding anomalies in metrics
* Rate limiting / counters
* String transformations

💡 They’re not expecting LeetCode-hard — more like **clean, efficient solutions**.

---

## 2. Debugging & Code Understanding

You might get:

* A broken script (Python, Bash, or pseudo-code)
* Asked: *“Why does this fail?”* or *“Fix it”*

Focus areas:

* Edge cases
* Off-by-one errors
* Bad assumptions
* Performance issues

---

## 3. DevOps/SRE Concepts

This is where you differentiate yourself.

Expect questions around:

### 🔧 Linux & Systems

* Processes, memory, CPU usage
* `top`, `ps`, `netstat`, `grep`
* File permissions

### 🌐 Networking

* HTTP vs HTTPS
* DNS basics
* Load balancing concepts

### 📦 Containers & CI/CD

* Docker basics (images vs containers)
* CI/CD pipelines (GitHub Actions, GitLab CI)
* Deployment strategies (rolling, blue-green)

### ☁️ Cloud (Very likely AWS-focused)

* EC2, S3 basics
* Scaling (Auto Scaling Groups)
* Monitoring (CloudWatch-like concepts)

### 📊 Observability

* Logs vs metrics vs traces
* Alerting basics
* SLIs, SLOs, SLAs

---

## 4. SRE Mindset Questions

These are subtle but important.

Examples:

* “System is slow — what do you check first?”
* “How do you design a reliable system?”
* “How do you reduce downtime?”

They’re testing:

* Structured thinking
* Prioritization
* Trade-offs

---

# ⚡ How to Prepare (High ROI Plan)

## 🔹 1. Practice Codility-style Problems (IMPORTANT)

Focus on:

* Arrays & strings
* Hash maps
* Basic math/logical problems

Good platforms:

* Codility lessons (if you have access)
* HackerRank (easy–medium)

👉 Practice writing:

* Clean code
* Fast solutions (O(n), not O(n²))

---

## 🔹 2. Master Log Parsing (VERY RELEVANT)

As an SRE, logs = everything.

Practice:

```python
# Example pattern
for line in logs:
    if "ERROR" in line:
        ...
```

Also:

* Extract fields
* Count occurrences
* Detect patterns

---

## 🔹 3. Revise Core DevOps Concepts

Don’t go too broad — go **practical**.

Focus on:

* How a request flows (DNS → LB → server)
* What happens when a server crashes
* How CI/CD works end-to-end

---

## 🔹 4. Practice Bash/Python Scripting

You may need to:

* Parse files
* Automate tasks
* Process data

Know:

* Loops
* File handling
* Basic shell commands

---

## 🔹 5. Think in “Production Mode”

Always ask yourself:

* What breaks?
* What scales?
* What fails under load?

---

# 🧩 Example Question (Very Likely Style)

> Given a list of log entries, return the IP with the most failed requests.

They’re testing:

* Parsing
* Counting
* Efficiency

---

# 🚀 During the Test

* Start with the easiest question
* Get something working first, then optimize
* Handle edge cases:

  * empty input
  * large input
  * duplicates
* Watch time — don’t get stuck

---
