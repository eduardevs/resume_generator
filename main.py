from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_cv(request: Request):
    data = {
        "request": request,  # Required by Jinja2Templates
        "cv": {
            "nom": "Doe",
            "prenom": "John",
            "title": "Security Analyst",
            "skills": ["SOC Monitoring", "SIEM", "Python", "Threat Hunting"],
            "experience": [
                {"company": "ITrust", "role": "SOC Analyst", "duration": "2022–2024"},
                {"company": "CyberGuard", "role": "Intern", "duration": "2021–2022"},
            ],
        }
    }

    return templates.TemplateResponse("cv.html", data)

# object for jinja
cv = {
    "nom": "Doe",
    "prenom": "John",
    "titre": "Ingénieur Sécurité Informatique",
    "email": "john.doe@example.com",
    "telephone": "+33 6 12 34 56 78",
    "linkedin": "linkedin.com/in/johndoe",
    "profil": "Ingénieur spécialisé en cybersécurité avec 5 ans d'expérience dans le monitoring SOC.",
    "competences": ["SIEM", "Analyse de logs", "Réponse aux incidents", "Python", "ISO 27001"],
    "experiences": [
        {
            "poste": "Analyste SOC",
            "entreprise": "ITrust",
            "date_debut": "Jan 2022",
            "date_fin": "Présent",
            "description": "Analyse des alertes, amélioration continue du périmètre, rédaction de rapports mensuels."
        },
        {
            "poste": "Stagiaire cybersécurité",
            "entreprise": "Orange Cyberdefense",
            "date_debut": "Avr 2021",
            "date_fin": "Sep 2021",
            "description": "Participation à des projets de sécurisation de systèmes et analyse de vulnérabilités."
        }
    ],
    "formations": [
        {"diplome": "Master Cybersécurité", "ecole": "Université de Toulouse", "annee": "2021"},
        {"diplome": "Licence Informatique", "ecole": "Université de Lyon", "annee": "2019"}
    ],
    "langues": [
        {"nom": "Français", "niveau": "Natif"},
        {"nom": "Anglais", "niveau": "Courant"}
    ]
}
