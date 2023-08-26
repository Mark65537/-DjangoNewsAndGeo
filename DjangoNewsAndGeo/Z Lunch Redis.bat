@echo off
cd /d %~dp0Redis-7.0.12/
redis-server.exe redis.conf
pause
