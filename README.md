# First API (FastAPI)

Minimal FastAPI example with two endpoints and tests.

Run locally:

```powershell
cd 'e:\FastAPI\First API'
python -m venv .venv; .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

To push to GitHub (after creating a remote repository):

```powershell
git remote add origin <your-git-url>
git branch -M main
git push -u origin main
```

LinkedIn: a ready-to-use post is included in `LINKEDIN_POST.md`.
