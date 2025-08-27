# Pharma Safety HMI — Next.js + FastAPI

Frontend: Next.js (React + Tailwind + Konva + ECharts)  
Backend: FastAPI (history + AI summarize)

## Local run

### Backend
```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-... # optional for AI
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd apps/web
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
npm run dev
# open http://localhost:3000
```

Put your PNGs in apps/web/public/images/
