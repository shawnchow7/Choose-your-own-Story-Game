# Interactive Story Generator

A full-stack application that generates interactive choose-your-own-adventure stories using OpenAI's API.

## Project Structure

```
Story-Generator/
├── backend/          # FastAPI backend
└── frontend/         # React frontend
```

## Quick Start

### Prerequisites
- Python 3.8+ (for backend)
- Node.js 16+ (for frontend)
- OpenAI API key

### Backend Setup
```bash
cd backend
uv sync
cp .env.example .env
# Add your OpenAI API key to .env
uv run main.py
```

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```



## Features

- **AI-Powered Story Generation**: Uses OpenAI's GPT model to create engaging stories
- **Interactive Gameplay**: Choose-your-own-adventure format with multiple paths
- **Real-time Updates**: Live status updates during story generation
- **Session Management**: Tracks user sessions with cookies
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy (Database ORM)
- LangChain (AI integration)
- SQLite (Database)

**Frontend:**
- React (UI library)
- Vite (Build tool)
- React Router (Navigation)
- Axios (HTTP client)

## API Documentation


## Contributing

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
