FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

USER vscode

COPY --chown=vscode:vscode requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
