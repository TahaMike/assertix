---

# ⚙️ Setup & Usage Guide

## 🔒 Prerequisites (Mandatory)

Before using WORM Agent, ensure the following:

### 1. Install Ollama

Download and install from: [Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

Verify installation:

```powershell
ollama --version
```

---

### 2. Pull Required Model

This project is designed to work with:

```powershell
ollama pull deepseek-coder:6.7b
```

> ⚠️ Constraint: The agent expects a **code-capable model**. Using other models may degrade output quality or break formatting.

---

### 3. Ensure Ollama is Running

```powershell
ollama serve
```

If already running, you may see a port error—that’s fine.

---

# 🧩 Step-by-Step: Add `worm` to System PATH

## Step 1 — Verify Project Location

Example:

```text
..\worm-agent
```

Ensure it contains:

```text
worm.py
worm.bat
core/
```

---

## Step 2 — Validate `worm.bat`

Open `worm.bat` and ensure:

```bat
@echo off
python "%~dp0worm.py" %*
```

---

## Step 3 — Add Folder to PATH

### Option A — GUI Method (Recommended)

1. Press **Win + S**
2. Search → *Environment Variables*
3. Click → **Edit the system environment variables**
4. Click → **Environment Variables**
5. Under **User variables**, find `Path` → click **Edit**
6. Click **New** → add:

```text
..\worm-agent
```

7. Click **OK** → **OK** → **OK**

---

### Option B — PowerShell Method

```powershell
[Environment]::SetEnvironmentVariable(
  "Path",
  [Environment]::GetEnvironmentVariable("Path", "User") + ";..\worm-agent",
  "User"
)
```

---

## Step 4 — Restart Terminal (Critical)

* Close VS Code completely
* Reopen terminal

---

## Step 5 — Verify Installation

```powershell
where worm
```

Expected output:

```text
..\worm-agent\worm.bat
```

---

# 🚀 Usage

## Basic Command

```powershell
worm conftest.py "optimize and clean code"
```

---

## With Piped Input

```powershell
type conftest.py | worm "refactor and improve structure"
```

---

# ❌ If `worm` Command Does NOT Work

## 1. Try Direct Execution

```powershell
..\worm-agent\worm.bat conftest.py "fix bugs"
```

---

## 2. Temporary PATH Fix (Session Only)

```powershell
$env:Path += ";..\worm-agent"
```

Then:

```powershell
worm conftest.py "optimize code"
```

---

## 3. Use PowerShell Alias (Quick Fix)

```powershell
Set-Alias worm "..\worm-agent\worm.bat"
```

---

## 4. Verify File Extension

Run:

```powershell
ls ..\worm-agent
```

Ensure:

```text
worm.bat
```

NOT:

* `worm.bat.txt` ❌
* `worm` ❌

---

# ⚠️ Common Issues

### Port Already in Use (Ollama)

```text
listen tcp 127.0.0.1:11434: bind error
```

✔ Means Ollama is already running → ignore

---

### `worm not recognized`

✔ PATH not set correctly
✔ Terminal not restarted
✔ `.bat` not detected

---

### Broken Virtual Environment

If pip fails:

```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
```

---

# 🧠 Summary

To run WORM Agent successfully:

* ✔ Ollama installed and running
* ✔ `deepseek-coder:6.7b` model pulled
* ✔ `worm-agent` folder added to PATH
* ✔ Terminal restarted
* ✔ Command verified using `where worm`

---

# 🔥 Pro Tip

For a cleaner setup (no `.bat`, no PATH issues), convert this into a CLI tool using:

```powershell
pip install -e .
```

---