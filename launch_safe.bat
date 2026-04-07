@echo off
setlocal

if exist venv\Scripts\python.exe (
    set PYTHON=venv\Scripts\python.exe
) else (
    set PYTHON=python
)

echo Running Django system checks...
%PYTHON% manage.py check
if errorlevel 1 goto :failed

echo Running smoke tests for pages and journal...
%PYTHON% manage.py test pages journal
if errorlevel 1 goto :failed

echo All checks passed. Starting development server...
%PYTHON% manage.py runserver
goto :eof

:failed
echo.
echo Pre-launch verification failed. Server was not started.
exit /b 1
