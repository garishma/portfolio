from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn

from portfolio_data import (
    IDENTITY, SUMMARY, STATS, INDUSTRIES,
    COMPETENCIES, EXPERIENCE, ACHIEVEMENTS,
    CERTIFICATIONS, EDUCATION
)

app = FastAPI(title="Garishma Gupta Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request":        request,
        "identity":       IDENTITY,
        "summary":        SUMMARY,
        "stats":          STATS,
        "industries":     INDUSTRIES,
        "competencies":   COMPETENCIES,
        "experience":     EXPERIENCE,
        "achievements":   ACHIEVEMENTS,
        "certifications": CERTIFICATIONS,
        "education":      EDUCATION,
    })


@app.get("/resume")
async def download_resume():
    path = Path("static/resume.pdf")
    if path.exists():
        return FileResponse(
            path,
            media_type="application/pdf",
            filename="Garishma_Gupta_Resume.pdf"
        )
    return {"error": "Place resume.pdf in static/ folder"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
