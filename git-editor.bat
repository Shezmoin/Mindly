@echo off
REM This script is used as the git editor for interactive rebase
REM It automatically marks commits with "AI" for reword and saves

if exist "%1" (
    REM Replace "pick" with "reword" for the commit with AI traces
    powershell -Command "(Get-Content '%1') -replace 'pick 5f71e48', 'reword 5f71e48' | Set-Content '%1'"
)
