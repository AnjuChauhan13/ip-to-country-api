#  IP to Country API - FastAPI

This is a simple API built using FastAPI that returns the **country**, **city**, and **continent** of a given IP address using MaxMind's GeoLite2 database.

---

##  How to Run

1. **Create virtual environment**:

```bash
python -m venv venv

uvicorn main:app --reload

