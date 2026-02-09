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

## Usage Guide

Altus is designed to be used directly from the terminal with a simple and explicit syntax.

### Basic Usage

```bash
altus <file> "<prompt>"

altus main.py "refactor this code to be more readable"










