# AI-OS V2.6 Milestone Management Design Scope

## Version

AI-OS V2.6.0

---

# 1. Purpose

Add milestone management capability between Goal and Task.

Current:

Goal
↓
Task
↓
Execution

V2.6:

Goal
↓
Milestone
↓
Task
↓
Execution

---

# 2. New Module

Add:

core/milestone/

Core component:

MilestoneManager

---

# 3. Responsibility

MilestoneManager is responsible for:

- Creating milestones
- Managing milestone status
- Tracking milestone progress

---

# 4. Status Model

created

↓

active

↓

completed

---

# 5. Data Model

Example:

{
    "milestone_id": "m001",
    "goal_id": "goal_001",
    "title": "核心智能层完成",
    "status": "active",
    "progress": 30
}

---

# 6. Data Flow

GoalManager

↓

MilestoneManager

↓

TaskPlanner

↓

TaskManager

↓

Executor

---

# 7. Boundary

Not responsible:

- Automatically creating tasks
- Automatically executing tasks
- Modifying user goals
- Making strategic decisions

---

# Freeze Rule

Only implement features inside this boundary.