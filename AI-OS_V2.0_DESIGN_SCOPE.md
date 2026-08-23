# AI-OS V2.0 Confirmed Task Loop Design Scope

## Version

AI-OS V2.0.0

---

# 1. Module Position

Current:

V2.0 adds:
    ↓
    ↓
    ↓
    ↓

---

# 2. Core Purpose

Build the confirmed task generation loop.

Goal:

After user approval,
AI-OS can convert an approved suggestion into a structured task.

---

# 3. Permission Boundary

Only when:

can the system continue to task generation.

Without confirmation:
↓

---

# 4. Responsibility

## TaskPlanner

Responsible for:

- Convert confirmed suggestions into task data
- Generate structured task information

Example:

Input:

Output:

---

# 5. Not Responsible

TaskPlanner does NOT:

- Ask for confirmation
- Automatically approve
- Execute tasks
- Control devices
- Replace TaskManager

---

# 6. Data Flow
    ↓
    ↓
    ↓
    ↓
    ↓
    ↓

---

# 7. User Control Principle

AI can:

- Suggest
- Wait for approval
- Generate tasks after approval

AI cannot:

- Skip confirmation
- Create unauthorized tasks
- Execute without permission

---

# 8. V2.0 Implementation Scope

Only implement:

Functions:

- create_task_plan()

---

# 9. Excluded Scope

Not included:

- Autonomous task creation
- Autonomous execution
- Complex planning engine
- Agent loops

---

# Freeze Rule

Only implement features inside this boundary.
