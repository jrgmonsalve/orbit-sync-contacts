from fastapi import FastAPI, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from models import RequestLog

async def save_request_log(request: Request, db: Session = SessionLocal()):
    """Save a log of the request in the database"""
    log = RequestLog(
        method=request.method,
        url=str(request.url),
        path=str(request.url.path),
        headers=dict(request.headers),
        body=await request.body(),
    )
    db.add(log)
    db.commit()
    db.refresh(log)

async def middleware(request: Request, call_next):
    """FastAPI middleware that saves a log of the request"""
    response = await call_next(request)
    await save_request_log(request)
    return response