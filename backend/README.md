# Story Generator Backend

A FastAPI backend for generating interactive choose-your-own-adventure stories using OpenAI's API.

## Setup

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your OpenAI API key:
   ```
   OPEN_AI_KEY=your_actual_openai_api_key_here
   ```

3. **Run the server:**
   ```bash
   uv run main.py
   ```

The API will be available at http://localhost:8000

## API Documentation

Visit http://localhost:8000/docs for interactive API documentation.

## Environment Variables

- `OPEN_AI_KEY`: Your OpenAI API key (required)
- `DATABASE_URL`: Database connection string (default: SQLite)
- `API_PREFIX`: API route prefix (default: /api)
- `DEBUG`: Enable debug mode (default: True)
- `ALLOWED_ORIGINS`: CORS allowed origins for frontend
