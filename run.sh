#!/bin/zsh
cd "$(dirname "$0")"

echo "Starting backend (FastAPI) on 8000..."
./.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000 > uvicorn.log 2>&1 &
BACKEND_PID=$!

sleep 2

# Check backend
if curl -s http://127.0.0.1:8000/ > /dev/null; then
  echo "Backend is up ✅"
else
  echo "Backend failed ❌. Open uvicorn.log to see why."
  kill $BACKEND_PID 2>/dev/null || true
  exit 1
fi

echo "Starting UI (Streamlit) on 8501..."
# Start streamlit in background so we can open browser after it's up
./.venv/bin/python -m streamlit run ui.py --server.port 8501 > streamlit.log 2>&1 &
STREAMLIT_PID=$!

# Wait for streamlit to start
for i in {1..20}; do
  if curl -s http://127.0.0.1:8501/ > /dev/null; then
    echo "UI is up ✅"
    open "http://127.0.0.1:8501"
    break
  fi
  sleep 0.5
done

echo ""
echo "App is running. To stop: close this window OR run: kill $BACKEND_PID $STREAMLIT_PID"
echo ""

# Keep script alive so background services don’t die
wait $STREAMLIT_PID

echo "Stopping backend..."
kill $BACKEND_PID 2>/dev/null || true
