# Databases — University of Tartu, Fall 2026

## Start Lab 0

1. Click **Open in GitHub Codespaces** on this repository and create a Codespace.
2. Wait for Codespaces to finish its automatic setup. Its setup output will say that PostgreSQL is ready.
3. Open [`lab0/Lab0-PostgreSQL-basics.ipynb`](lab0/Lab0-PostgreSQL-basics.ipynb).
4. If VS Code asks, select the provided Python kernel, then run the cells from top to bottom.

The first executable cells check the connection and run `SELECT version()`. PostgreSQL is already running: do **not** run Docker Compose, configure pgAdmin, install PostgreSQL locally, or write Python connection code for Lab 0.

The course database uses `student` / `student` in an isolated Codespaces teaching environment. These credentials are intentionally simple and are not production credentials.

## Instructor troubleshooting

- If the connection cell fails just after Codespaces opens, wait 30 seconds and rerun it. The setup waits for PostgreSQL, but an initial image pull can take longer.
- To reset a student's Lab 0 table, have them use the notebook's reset cell. From the workspace terminal, `python lab0/reset-lab0.py` performs the same limited reset.
- Inspect services with `docker compose ps` only when troubleshooting. pgAdmin is optional: `docker compose --profile tools up -d pgadmin` starts it for later exploration.
- A corrupt development database volume is best handled by recreating the Codespace. Never use the teaching credentials outside this isolated environment.

Later relational, MongoDB, and Neo4j labs will be added or redesigned separately.
