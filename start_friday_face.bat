@echo off
cd /d C:\LimraAI

start py friday_face.py
timeout /t 2 >nul

py wake_chat.py