#!/bin/bash

# Start FastAPI server
(cd backend && source venv/bin/activate && uvicorn main:app --reload) &

# Start Next.js app
(cd frontend && npm run dev)