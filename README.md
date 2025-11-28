# 🤖 Versatile Multi-Tool LangChain Agent (Ollama Powered)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangChain v0.2+](https://img.shields.io/badge/LangChain-v0.2%2B-green)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Project Description

This repository contains a highly versatile and reliable multi-tool agent built on the LangChain framework. It is designed to operate entirely on a local server environment, using **Ollama** to host the **Gemma 3** model.

The core feature of this project is demonstrating how to build a stable **ReAct Agent** capable of successfully parsing and executing complex commands (like multi-argument tool calls and chained actions) with open-source LLMs, a common challenge in self-hosted AI applications.

---

## ✨ Key Features & Toolset

The agent is equipped with a comprehensive set of internal and external tools:

| Category | Tool | Description |
| :--- | :--- | :--- |
| **Multimodal / Vision** | `caption_image_func` | Analyzes local image files (e.g., satranç konumu) and provides a descriptive answer via the Ollama multimodal API. |
| **Media Processing** | `youtube_transcript_func` | Downloads audio from a YouTube URL (`yt-dlp`) and transcribes the content using **Whisper**. |
| **Information Retrieval** | `general_web_search`, `academic_search`, `wikipedia_search` | External search capabilities via DuckDuckGo, ArXiv, and Wikipedia. |
| **File & I/O** | `file_download_func` | Downloads files by ID from a specific URL and provides content previews (Excel, JSON, Audio). |
| **Code Execution** | `python_repl_tool` | Executes arbitrary Python code for complex calculations and data analysis, replacing unreliable math functions. |
| **API Integration** | `WeatherInfoTool` | Fetches current weather information for a given location. |
| **Orchestration** | `ReAct AgentExecutor` | Manages the decision-making loop, ensuring the right tool is called at the right time. |

---

## ⚙️ Setup and Installation

### Prerequisites

1.  **Python:** Python 3.11 or newer.
2.  **Ollama:** Ollama server must be running and accessible via a public URL (e.g., Cloudflare Tunnel) or locally (`http://localhost:11434`).
    * **Model:** Ensure you have a powerful instruction-following model installed, such as `gemma3:27b` or `llama3:8b`.
3.  **System Dependencies:**
    ```bash
    # For YouTube download and audio processing
    sudo apt install yt-dlp ffmpeg  # or use brew/choco
    ```

### Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
# (Assuming requirements.txt contains:
# langchain-ollama
# langchain-community
# langchain-core
# pydantic
# duckduckgo-search
# arxiv
# wikipedia
# whisper / openai-whisper
# pandas, openpyxl, pillow, requests
# ... and any other dependencies)
