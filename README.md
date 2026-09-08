# 🤖 26AI — Personal AI Assistant

> **A personal AI assistant designed to interact with the user through voice, natural language, and system automation.**

## 📌 Overview

**26AI** is a personal AI assistant project developed by **Abdul Naser** as an exploration of Artificial Intelligence, Natural Language Processing, Large Language Models, voice interaction, and desktop automation.

The project combines **speech recognition, LLM technology, Ollama, text-to-speech, and Python-based automation** to create an AI assistant capable of understanding user commands and interacting with the Windows environment.

The assistant is designed around **26**, with **Friday** serving as the underlying voice engine.

---

## ✨ Features

* 🤖 AI-powered conversational interaction
* 🎙️ Voice command recognition
* 🗣️ Text-to-speech responses
* 🧠 Large Language Model integration
* 🦙 Local LLM support through Ollama
* 🖥️ Windows application launching
* ⚙️ System command execution
* 🔍 Application detection and search
* 🎯 Command processing
* 🖥️ HUD interface integration
* 🔊 Voice feedback
* 📊 Visual assistant status

---

## 🧠 Technology Stack

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| Python                  | Core development               |
| Ollama                  | Local LLM runtime              |
| LLM                     | Natural-language understanding |
| Speech Recognition      | Voice input                    |
| Piper TTS               | Voice output                   |
| PySide6 / PyQt6         | Graphical interface            |
| Windows APIs / Commands | System automation              |

---

## 🏗️ System Architecture

```text
              USER
                │
        Voice / Text Input
                │
                ▼
       Speech Recognition
                │
                ▼
          26AI CORE
                │
        ┌───────┴───────┐
        │               │
        ▼               ▼
     Ollama          Command
      + LLM          Processing
        │               │
        └───────┬───────┘
                │
                ▼
       Action / Response
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
 Windows Applications   System
                       Controls
        │                │
        └───────┬────────┘
                ▼
           26AI Response
                │
                ▼
             Piper
               TTS
                │
                ▼
          Voice Output
```

---

## 🦙 Role of Ollama

Ollama provides the local environment for running the selected Large Language Model.

Instead of relying entirely on an external AI service, 26AI can communicate with a locally running model through Ollama.

This allows the project to explore:

* Local LLM inference
* Natural-language processing
* Prompt-based interaction
* AI command interpretation
* Local AI experimentation

---

## 🎙️ Voice Pipeline

The voice interaction follows a pipeline similar to:

```text
Microphone
    ↓
Speech Recognition
    ↓
User Command
    ↓
26AI
    ↓
Ollama / LLM
    ↓
Response / Action
    ↓
Piper TTS
    ↓
Speaker
```

---

## 🎯 Project Objectives

The primary objectives of 26AI are:

1. Build a personal AI assistant from the ground up.
2. Understand how LLMs can be integrated into applications.
3. Experiment with local LLMs using Ollama.
4. Implement voice-based interaction.
5. Explore NLP and command processing.
6. Connect AI with Windows automation.
7. Develop practical AI/ML engineering skills.

---

## 🚧 Development Status

**Status: Active Development**

26AI is an evolving personal project. Features, architecture, models, and capabilities may change as development continues.

---

## 🔮 Future Improvements

Planned improvements may include:

* Better contextual conversations
* Improved intent detection
* More advanced NLP processing
* Better command validation
* Expanded Windows automation
* Memory capabilities
* More intelligent application control
* Improved voice interaction
* Advanced HUD integration
* More local AI capabilities

---

## ⚠️ Repository Notice

This repository represents a personal educational and portfolio project.

Some components, configurations, implementation details, or private functionality may not be included in the public repository.

---

## 📜 Copyright & Usage

**Copyright © 2026 Abdul Naser. All rights reserved.**

This repository is provided for **educational and portfolio viewing purposes**.

**Reuse, redistribution, modification, republication, or commercial use requires permission from the author.**

The availability of this repository on GitHub does not transfer ownership or authorship of the project.

---

## 👨‍💻 Author

**Abdul Naser**

AIML Student | AI/ML Developer | Generative AI Enthusiast

---

**© 2026 Abdul Naser — All Rights Reserved.**

