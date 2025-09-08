# Version 2 Objective

Now that we know what metrics matter (based on version 1), I created a database in PostgreSQL that will house all of these metrics for the last 10 years along with some data with information of individual players and teams.

## Files

- `create_tables.sql` – SQL script to create all necessary tables:
  - `players` – basic player information
  - `player_stats` – yearly statistics per player
  - `teams` – team-level metrics and context

## Requirements

- **PostgreSQL**
- Optional: **pgAdmin 4**