# AI-OS V2.1 Task Commit Loop Design Scope

## Version

AI-OS V2.1.0

---

# 1. Module Position

Current:

V2.1 adds:
  ↓
  ↓

---

# 2. Core Purpose

Create the confirmed task submission loop.

Goal:

After user approval,
AI-OS can submit the generated task plan into TaskManager.

---

# 3. Permission Boundary

Only when:

can task submission continue.

Without confirmation:
↓

---

# 4. Responsibility

## TaskPlanner

Responsible for:

- Generate task plan
- Submit confirmed task plan

---

## TaskManager

Responsible for:

- Create task records
- Manage task lifecycle
- Store task state

---

# 5. Data Flow
    ↓
    ↓
    ↓
    ↓
    ↓
    ↓

---

# 6. Not Responsible

V2.1 does NOT:

- Automatically approve suggestions
- Create tasks without confirmation
- Execute tasks automatically
- Control devices
- Replace Executor

---

# 7. User Control Principle

AI can:

- Suggest
- Wait for approval
- Submit approved tasks

AI cannot:

- Skip confirmation
- Create unauthorized tasks
- Execute without permission

---

# 8. Implementation Scope

Only modify:

Possible changes:

- TaskPlanner task commit interface
- TaskManager receiving interface

---

# 9. Excluded Scope

Not included:

- Automatic execution
- Autonomous Agent loop
- Device actions
- Complex planning system

---

# Freeze Rule

Only implement features inside this boundary.
