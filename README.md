# Tokemon Demo

A web application for counting tokens across multiple LLM providers. Built as a demonstration for the [tokemon](https://github.com/lymagics/tokemon) Python library.

## Features

- Count tokens for OpenAI, Anthropic, Google AI, and xAI models
- Clean, responsive UI with dark/light mode
- Single-page application with FastAPI backend

## Supported Providers

| Provider | API Key Required |
|----------|------------------|
| OpenAI | No (offline) |
| Anthropic | Yes |
| Google AI | Yes |
| xAI | Yes |

Models are fetched dynamically from each provider's API at runtime.

## Quick Start

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
make dev
```

Open http://localhost:8000

### Docker

```bash
# Build
docker build -t tokemon-demo .

# Run
docker run -p 8080:8080 tokemon-demo
```

Open http://localhost:8080

## Environment Variables

Required only for non-OpenAI providers:

```
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
XAI_API_KEY=
```

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Granian](https://github.com/emmett-framework/granian) - ASGI server
- [tokemon](https://github.com/lymagics/tokemon) - Token counting library

## License

MIT
