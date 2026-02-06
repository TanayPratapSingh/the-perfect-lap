# Overview

Welcome to your group project repository!  Please follow these instructions:
- All project management related files belong in the the `admin` directory.  More information on these files below.
- Your project proposal will be submitted as `proposal.md` in the `proposal` directory.  You will find the rubric for the proposal there.
- Your presentation will either be uploaded (as pdf or ppt) or linked in a file named `presentation_link.md` in the `presentation` directory.  You will find the rubric for the presentation there.
- Your final project narrative named `final.md` and *all supporting jupyter notebooks* will go in the `final` directory.  You will find the rubric for the final narrative there.
- There will be new commits to the project every week henceforth.  Lack of regular activity will reduce your final grade, even if your project is wonderful in the end!

The following project management guide explains how we will track and manage our group project throughout the semester.
Our approach is intentionally lightweight — the goal is to form strong project management habits without adding unnecessary tool overhead.

---

# Project Management

## Why We Do This

* **Keep the team aligned** — Everyone should know the project vision, the current plan, and recent progress at all times.
* **Document decisions and changes** — Projects always evolve. A clear record of what changed, when, and why prevents confusion and helps with grading.
* **Support AI-assisted work** — Modern AI tools are powerful, but their memory is limited. Having structured, up-to-date documents gives AI agents the context they need to work effectively with you, even after restarts or when using multiple agents.
* **Integrate with git** — By keeping planning artifacts in the repository, you can link tasks in the plan directly to your commits, making it easy to correlate planning with execution.

The key is not to have a “perfect” system — it’s to **use a system reliably**.

---

## The Two Core Documents

All documents live at the top level of your project repository.

### 1. `VISION.md`

* **Purpose:** Defines the project’s “North Star” — what you are trying to accomplish and why.
* **Stability:** Should remain unchanged unless there’s a major pivot.
* **Version History:** If the vision changes, archive the old vision at the bottom with the date and reason for the change.

### 2. `WORKPLAN.md`

* **Purpose:** Outlines the full project plan and logs important changes.

* **Three Sections:**

  * **Active Plan:** The complete and current plan. Includes *all* tasks (completed and not), with status marked in place.
  * **Weekly Tasks:** Append weekly entries to establish priorities for the _following_ week.
  * **Log:** Append-only log of work done and significant changes.  "Work done" includes any work on tasks in progress (:hourglass_flowing_sand:) that have not been completed.  "Significant changes" include new tasks, significant revisions, abandoned or blocked tasks, and pivots (when large sections of the plan are abandoned). Routine completions do not need to be logged.

* **Task Status Tags:**

   _In the **Active Plan** section_

  * ✅ `:white_check_mark:` DONE
  * ⏳ `:hourglass_flowing_sand:` IN PROGRESS

  _In the **Log** section_

  * 🚫 `:no_entry_sign:` BLOCKED
  * ❌ `:x:` ABANDONED
  * 🆕 `:new:` NEWLY ADDED
  * 🔄 `:arrows_counterclockwise:` REVISED scope or details

*Note: Github supports a [wide range of emojis](https://gist.github.com/rxaviers/7360908) - Use what you want!*

* **Hierarchy:** Use nested lists to break down milestones into tasks and subtasks. Use stable IDs (e.g., `M1-T2a` or `M1.CLEAN`) to allow insertion of new items without renumbering. Use whatever makes sense for you - there is no "right way" here; only something that works.

* **Responsible Party:** Every task in the **Weekly Tasks**, and every task with :hourglass_flowing_sand: or :white_check_mark: in the **Active Plan** must list the person(s) responsible for the task.  Planned tasks may or may not include a responsible party.

* **Weekly Tasks:** The **Active Plan** provides a conceptual breakdown of tasks; the **Weekly Tasks** keeps track of the temporal execution of tasks on an ongoing basis. 

---

## How to Maintain These Documents

### VISION.md

1. Write the initial vision at the top of the document in a “Current Vision” section.
    * Less detailed than a project proposal
    * Should contain project title, stakeholder(s), problem statement, and envisioned solution
    * Add as much detail as you think is necessary to communicate your project goals to an AI
2. If a major pivot happens:
   * Move the old vision to the “Version History” section with date and reason.
   * Write the new vision at the top.

### WORKPLAN.md

1. Keep the **Active Plan** current:

   * Add new tasks with a unique identifier (usually something like `M2-T4` - the id should never change once assigned).  Note new tasks in the Log with 🆕 to draw attention.
   * Revise tasks as necessary, and note them with :arrows_counterclockwise: in the Log. 
   * Update statuses in the active plan as work progresses (from :hourglass_flowing_sand: to :white_check_mark:); make sure to indicate the responsible parties for the task.
   * Remove tasks that are abandoned and tag them in the **Log** with :x:. 

2. At the end of each week:

   * Update statuses in **Active Plan**.
   * Append new tasks for the **Weekly Tasks** for the next week.
   * Add any work in progress to the **Log** to help you, the team, and your professor keep track of work that doesn't necessarily result in a completed task.
   * Add **Log** entries to note changes (decision, pivot, scope change, abandoned, blocker).

3. If the project changes significantly:

   * For a **pivot**: If the entire plan changes, archive the previous plan into Log under a “Project Pivot” heading, then start fresh.
   * For **major adaptations**: Note the change in the Log, adjust affected tasks in Active Plan, and tag them ❌ or 🔄.
   * For **minor additions**: Just add 🆕 tasks to the Active Plan.

---

## Using These Documents with AI

You can copy relevant sections of these files (or even the whole file) into AI prompts to:

* Summarize current status.
* Generate next-step suggestions.
* Identify blockers and propose solutions.
* Update the plan automatically.

Because these files are plain Markdown, they can be read, edited, and version-controlled by both humans and AI.

---

## Linking to Git Commit History

When you make commits:

* Reference the related WORKPLAN task in the commit message.
* Example:

```
git commit -m "✅ Implement PCA for feature reduction — relates to M2-T3"
```

* This creates a clear link between your commits and your project plan, making it easy to see how plans translate into work.

---

# Worked Examples


## 🔄 Example 1: Major Pivot (Dataset Change)

### **Before Pivot (Week 4)**

**WORKPLAN.md (Active Plan excerpt)**

```
## Active Plan

### Milestone 1: Data Prep
- [:white_check_mark:] M1.T1 — Acquire EHR dataset (Alice)
- [:hourglass_flowing_sand:] M1.T2 — Initial EDA (Team)
- [ ]  M1.T3 — Clean data (Bob)
- [ ]  M1.T4 — Feature engineering (Carol)

## Weekly Tasks
2025-09-12
- (Alice) M1.T1 — Acquire EHR dataset (Alice)
- (Team) M1.T2 — Initial EDA
2025-09-19
- (Team) M1.T2 — Initial EDA
```

---

### **Pivot Happens**

EHR dataset is unusable. Switch to predicting educational outcomes using a new dataset.
Cleaning and feature engineering remain relevant but are applied to the new data.

**WORKPLAN.md (Active Plan excerpt, after pivot)**

```
## Active Plan

### Milestone 1: Data Prep
- [✅] M1.T1 — Acquire EHR dataset (Alice)
- [✅] M1.T2 — Initial EDA (Team)
- [⏳] M1.T1A — Acquire educational dataset (Alice)
- [ ] M1.T2A — Initial EDA of new data (Team)
- [ ] M1.T3 — Clean data (Bob)   [revised]
- [ ] M1.T4 — Feature engineering (Carol)   [revised]

## Weekly Tasks
2025-09-12
- (Alice) M1.T1 — Acquire EHR dataset (Alice)
- (Team) M1.T2 — Initial EDA
2025-09-19
- (Team) M1.T2 — Initial EDA
2025-09-26
- (Alice) M1.T1A — Acquire educational dataset
- (Team) M1.T2A — Initial EDA

## Log
2025-09-21
- (Bob) ⏳ M1.T2 — Initial EDA - worked on this, scatterplots suggest this is simulated data? Contacted others...

2025-09-23 - **Major Pivot**
- (Team) ❌ M1.T2 — Abandoned EHR analysis due to simulated/unusable data
- (Alice) 🆕 M1.T1A — Added new task to acquire educational dataset
- (Team) 🆕 M1.T2A — Added to reflect new dataset
- (Bob, Carol) 🔄 M1.T3 and M1.T4 revised to work with educational data
```

---

# 🔄 Example 2: Minor Change (New Step Added)

### **Before Change (Week 3)**

**WORKPLAN.md (Active Plan excerpt)**

```
## Active Plan

### Milestone 2: Feature Engineering
- [⏳] M2.T1 — Extract sentiment scores from tweets (Bob)
- [ ]  M2.T2 — Aggregate scores into daily indicators (Alice)

## Weekly Tasks
2025-09-19
- (Bob)   M2.T1 — Extract sentiment scores
- (Alice) M2.T2 — Aggregate scores

## Log
2025-09-22
- (Bob) M2.T1 — Evaluated VADER; not happy with results.  Going to try https://huggingface.co/shhossain/all-MiniLM-L6-v2-sentiment-classifier

```
---

### **Minor Change Happens (Week 4)**

Team decides to add PCA dimensionality reduction.

**WORKPLAN.md (Active Plan excerpt, after change)**

```
## Active Plan

### Milestone 2: Feature Engineering
- [✅] M2.T1 — Extract sentiment scores from tweets (Bob)
- [⏳] M2.T2 — Aggregate scores into daily indicators (Alice)
- [ ]  M2.T3 — Implement PCA for dimensionality reduction (Carol)

## Weekly Plan
2025-09-26
- (Alice) M2.T2 — Aggregate scores
- (Carol) M2.T3 — Implement PCA

## Log
2025-09-22
- (Bob) ⏳ M2.T1 — Evaluated VADER; not happy with results. Going to try https://huggingface.co/shhossain/all-MiniLM-L6-v2-sentiment-classifier

2025-09-24
- (Alice) ⏳ M2.T2 — Tried aggregating scores, but uncertain how to handle different sentiment types from new model?

2025-09-26
- (Carol) 🆕 M2.T3 — Added PCA for dimensionality reduction
```


---

👉 Notice how this system keeps:

* **Active Plan** as the always-current, canonical view.
* **Weekly Tasks** as an append-only, forward-looking plan with names.
* **Log** as the history of work done, changes, pivots, and decisions.

---


## Final Notes

* Commit updates to these documents **at least once a week**. This is a large part of your project grade!
* Consistency matters more than perfection — aim for accurate, current, and readable updates.
* Use these documents as living tools, not just grading requirements. If you keep them well-maintained, they will make your work easier and your AI assistance more effective.
