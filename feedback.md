# Overall Feedback and Final Grade

This is a really interesting project, and it seems you've put a good deal of work in, though this has been inconsistent throughout the semester.  Your final writeup is comprehensive, though I would have preferred some graphical support in the report.  It's hard to infer much from performance metrics alone.

However, there is a fundamental problem that I called out during your presentation that you did not appear to grapple with in any specific way.  Your regression model is a model of *all* pit stops - from the best to the worst position.  The fact that you can predict the pit stop with a fair degree of accuracy undercuts the motivation for the project - to find the "optimal" (presumably meaning the pit stop that leads to the optimal position) first stop. The modeling you would need for this is quite a bit more sophisticated, but at the very least you could have done some early EDA to figure out if the timing of the first pit stop bore any relation to the final position, and then focused on selecting a pit stop to optimize position based on other features.

I've included an auto-generated contribution report below.  Based on this, it looks like Praveer did most of the work, supported by Atharva with Tanay putting in some work at the end.  Srikanth did very little, and I don't see anything from Titus (though Titus is indeed listed in the WorkPlan.md you created).  I've adjusted the "Weekly Update" grade for each individual to reflect this.

| Assessment Item | Praveer | Atharva | Tanay | Srikanth | Titus
|-----------------|-----------|---------|---|---|---|
| **Proposal (5 pts)** | 5 | 5 | 5 | 5 | 5
| **Weekly Updates (40 pts)** | 40 | 38 | 30 | 20 | 10
| **Final Presentation (5 pts)** | 5 | 5 | 5 | 5 | 5
| **Final Report (30 pts)** | 25 | 25 | 25 | 25 |25 
| **Total (80 pts)** | 75 | 73 | 65 | 55 | 45


# Contribution Report: group-project-team-omega

**Analysis Date:** 2025-12-29 21:49

**Project Period:** 2025-09-01 to 2025-12-08 (15 weeks)

## Administrative Documents

**WORKPLAN files detected:** admin/WORKPLAN_sample.md, proposal/WorkPlan1.md, proposal/WorkPlan.md, WorkPlan.md

**VISION files detected:** admin/new_vision.md, admin/vision.md, admin/VISION_sample.md

**Total admin document updates:** 9

| Author | Admin Doc Updates |
|--------|------------------|
| ath1812 | 3 |
| Tanay Pratap Singh | 3 |
| praveerbn | 2 |
| Srikanth M. | 1 |

## Effort Summary

| Author | Commits | % Commits | Lines Changed | % Lines | First Commit | Last Commit |
|--------|---------|-----------|---------------|---------|--------------|-------------|
| praveerbn | 11 | 34.4% | 766,103 | 52.1% | 2025-09-09 | 2025-12-11 |
| ath1812 | 10 | 31.2% | 704,441 | 47.9% | 2025-10-21 | 2025-12-03 |
| Tanay Pratap Singh | 8 | 25.0% | 532 | 0.0% | 2025-11-17 | 2025-12-11 |
| Joshua Introne | 2 | 6.2% | 22 | 0.0% | 2025-09-16 | 2025-10-07 |
| Srikanth M. | 1 | 3.1% | 20 | 0.0% | 2025-11-28 | 2025-11-28 |

**Total:** 32 commits, 1,471,118 lines changed

## Consistency Metrics

| Author | Active Weeks | Week Coverage | Late Work % | Consistency Grade |
|--------|--------------|---------------|-------------|-------------------|
| praveerbn | 7/15 | 47% | 45% | C - Fair |
| ath1812 | 3/15 | 20% | 50% | C - Fair |
| Tanay Pratap Singh | 2/15 | 13% | 75% | C - Fair |
| Srikanth M. | 1/15 | 7% | 0% | C - Fair |

**Metrics Explained:**
- **Active Weeks:** Number of weeks with at least one commit
- **Week Coverage:** Percentage of project weeks with activity
- **Late Work %:** Percentage of commits in the final 2 weeks
- **Consistency Grade:** Based on spread of work throughout the project

## Participation Alerts

⚠️ **Tanay Pratap Singh** was active in only 2 of 15 weeks (13% coverage)

⚠️ **Tanay Pratap Singh** completed 75% of their work in the final 2 weeks

⚠️ **ath1812** was active in only 3 of 15 weeks (20% coverage)

⚠️ **Srikanth M.** was active in only 1 of 15 weeks (7% coverage)



## Weekly Activity Timeline

```
Week         | Joshua Int | Srikanth M | Tanay Prat | ath1812    | praveerbn 
-------------------------------------------------------------------------------
2025-09-01   | .......... | .......... | .......... | .......... | ..........
2025-09-08   | .......... | .......... | .......... | .......... |     1     
2025-09-15   |     1      | .......... | .......... | .......... | ..........
2025-09-22   | .......... | .......... | .......... | .......... |     1     
2025-09-29   | .......... | .......... | .......... | .......... | ..........
2025-10-06   |     1      | .......... | .......... | .......... | ..........
2025-10-13   | .......... | .......... | .......... | .......... | ..........
2025-10-20   | .......... | .......... | .......... |     4      | ..........
2025-10-27   | .......... | .......... | .......... | .......... |     1     
2025-11-03   | .......... | .......... | .......... | .......... | ..........
2025-11-10   | .......... | .......... | .......... | .......... | ..........
2025-11-17   | .......... | .......... |     2      |     1      |     2     
2025-11-24   | .......... |     1      | .......... | .......... |     1     
2025-12-01   | .......... | .......... | .......... |     5      |     1     
2025-12-08   | .......... | .......... |     6      | .......... |     4     
```
