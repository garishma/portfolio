# Garishma Gupta — Portfolio

A production-ready cinematic executive portfolio built with FastAPI, Jinja2, Three.js, and GSAP.

---

## Quick Start (Windows)

### Step 1 — Place your assets
Copy these files into the correct folders:

| Your file        | Paste it here                    |
|------------------|----------------------------------|
| hero-video.mp4   | static\video\hero-video.mp4      |
| portrait.jpg     | static\images\portrait.jpg       |
| resume.pdf       | static\resume.pdf                |

### Step 2 — Create a virtual environment
```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install dependencies
```cmd
pip install -r requirements.txt
```

### Step 4 — Run the server
```cmd
python main.py
```

Open your browser at: **http://localhost:8000**

---

## Project Structure

```
fastapi-portfolio/
├── main.py                  ← FastAPI app + routes
├── portfolio_data.py        ← ALL resume content lives here
├── requirements.txt
├── templates/
│   └── index.html           ← Full portfolio HTML (Jinja2)
└── static/
    ├── css/
    │   └── style.css        ← Complete design system
    ├── js/
    │   ├── main.js          ← GSAP animations + interactions
    │   └── particles.js     ← Three.js particle layer
    ├── video/
    │   └── hero-video.mp4   ← Your talking head video
    ├── images/
    │   └── portrait.jpg     ← Your executive portrait
    └── resume.pdf           ← Resume download

```

## Editing Content

All portfolio content is in `portfolio_data.py` — edit that file alone to update
any text, experience, achievements, skills, or certifications. No HTML editing needed.

---

## Deploy to Render (free)

1. Push this folder to a GitHub repository
2. Go to https://render.com → New Web Service
3. Connect your GitHub repo
4. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click Deploy

## Deploy to Railway (free)

1. Push to GitHub
2. Go to https://railway.app → New Project → Deploy from GitHub
3. Railway auto-detects Python — set start command:
   `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Deploy

---

## Design Tokens

| Token       | Value     |
|-------------|-----------|
| Navy Deep   | `#0B1120` |
| Charcoal    | `#1C2333` |
| Platinum    | `#A8B4C8` |
| Gold Accent | `#C9A84C` |
| Display     | Playfair Display |
| Body        | Inter |
