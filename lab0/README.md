# Lab 0 — PostgreSQL basics

Open **`Lab0-PostgreSQL-basics.ipynb`** in Codespaces and run its cells from top to bottom. PostgreSQL is already running: there is no Docker command, local database installation, pgAdmin setup, or Python tutorial to complete first.

## Resetting your work

The notebook's **Reset and create the practice table** cell is safe to run at any time. It drops only `lab0_books`, then creates it again. Afterwards, run the remaining cells from the insert-data step onward.

An instructor can also run this inside the workspace container:

```bash
python lab0/reset-lab0.py
```

## Optional pgAdmin

pgAdmin is not needed for Lab 0. Later, an instructor may start it with `docker compose --profile tools up -d pgadmin`, then open port 8080. Sign in with `student@dbdm.local` / `student`; the course server is already listed. These deliberately simple credentials are for this isolated teaching environment only. Never reuse them for a real system.
