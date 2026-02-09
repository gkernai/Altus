# Altus

Altus is a terminal-first AI coding assistant designed to integrate directly into a developer’s local workflow.

Instead of pulling developers into chat interfaces, Altus lives where real work happens: the command line.

---


## AI Provider

Altus currently uses Google AI Studio (Gemini models) as its backend provider.

Altus acts as a thin client:
- It does not bundle or distribute any models
- All requests are made using the user's own API key
- Model usage is fully subject to Google AI Studio's terms of service

The provider layer is intentionally kept minimal to allow future support
for additional AI backends.

## API Key Setup (Required)

Altus requires an API key to communicate with the AI backend.
Without a valid API key, the tool will not run.

### Step 1: Get an API Key

Altus currently uses **Google AI Studio (Gemini models)**.

You can obtain an API key from:
https://aistudio.google.com/

---

### Step 2: Set the API Key (Ubuntu)

Set the API key as an environment variable:
***export GEMINI_API_KEY="your_api_key_here" ***


## What is Altus?

Altus is a CLI-based tool that connects large language models with your local development environment.
It is inspired by early ideas behind tools like OpenAI Codex, but focuses on **developer flow**, not conversation.

The goal is simple:
reduce friction between thinking, writing, and running code.

---

## Why Altus?

Most AI coding tools:
- break focus by switching contexts
- hide logic behind opaque UIs
- are hard to customize or extend

Altus takes a different approach:

- CLI-first, minimal interface
- Designed for iterative development
- Hackable and extensible by design
- Built with Unix philosophy in mind

---

## Features

- Prompt-driven code interaction
- Local environment awareness
- Lightweight architecture
- Modular structure for future expansion

> Note: Altus is under active development. Features and APIs may change.

---
## Installing Altus as a Command (Ubuntu)

To use `altus` as a global command in your terminal, you need to make the script executable
and add it to your `PATH`.

### Option 1: User-level installation (recommended)

This method does not require `sudo` and only affects your user.

```bash
chmod +x altus.py
mkdir -p ~/.local/bin
ln -s $(pwd)/altus.py ~/.local/bin/altus


## Usage Guide

Altus is designed to be used directly from the terminal with a simple and explicit syntax.

### Basic Usage

altus <file> "<prompt>"

altus main.py "refactor this code to be more readable"










