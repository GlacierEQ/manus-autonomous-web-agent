# Manus Autonomous Web Agent — Task Executor & Scheduler 🤖

> **TypeScript task executor and Python simulation harness for autonomous web agent workflows.**

[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6)]()
[![Python](https://img.shields.io/badge/Python-3.9+-blue)]()
[![Domain](https://img.shields.io/badge/Domain-Web%20Agents-blue)]()

---

## 🎯 For Recruiters & Hiring Managers

This repository implements the **Manus Autonomous Web Agent Executor** — scheduling and executing complex multi-step web interaction tasks (click, type, extract, navigate). It demonstrates:

- **TypeScript web task executor** with typed action payload validation
- **Task queue scheduling** prioritizing real-time user interactions
- **DOM element targeting** with selector resolution and fallback logic
- **Python simulation test harness** verifying execution flow offline

**Why this matters**: Autonomous web agents require robust task schedulers capable of handling asynchronous page responses and unexpected DOM states safely.

---

## 🔬 For Engineers & Technical Reviewers

### Core Components

| Component | Language | Purpose |
|---|---|---|
| `src/agent_executor.ts` | TypeScript | Typed web task queue and execution loop |
| `tests/test_agent_executor.py` | Python | Execution flow test wrapper |

---

## 🤖 ML/AI & Programmatic Mesh Integration

- **MCP Tool**: `execute_web_task()` — exposed for agent swarm task delegation
- **Mastermind Sidecar**: Connected to APEX Highway mesh
- **SHA-256 Integrity**: Tracked in `.integrity/file_hashes.json`

---

## ⚡ Quick Start

```bash
python3 tests/test_agent_executor.py
```
