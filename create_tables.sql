-- Players 
CREATE TABLE IF NOT EXISTS players (
    player_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(5) NOT NULL,
    birth_date DATE,
    draft_year INT,
	curr_team VARCHAR(5),
	recently_traded BOOLEAN
);

-- Stats per Season
CREATE TABLE IF NOT EXISTS player_stats (
    id SERIAL PRIMARY KEY,
    player_id VARCHAR(20) REFERENCES players(player_id),
    team VARCHAR(5),
    season INT NOT NULL,
    age INT,
	injury_risk INT,
    experience INT,
    games_played INT,
    carries INT,
    rushing_yards INT,
	half_ppr_sh DECIMAL(5,3),
	rushing_first_downs INT,
	target_share DECIMAL(5,3),
	wopr_x DECIMAL(5,3),
    receiving_yards_after_catch INT,
	targets INT,
	receiving_yards INT,
	receptions INT,
    receiving_tds INT,
    rushing_tds INT,
    fantasy_points_half_ppr DECIMAL(6,2)
);

-- Teams
CREATE TABLE IF NOT EXISTS teams (
    id SERIAL PRIMARY KEY,
    team VARCHAR(5),
    season INT NOT NULL,
    head_coach VARCHAR(100),
    offensive_coordinator VARCHAR(100),
    defensive_coordinator VARCHAR(100),
	qb_stability VARCHAR(20),
    strength_of_schedule INT,
    offensive_rank INT,
    defensive_rank INT,
    pace_of_play VARCHAR(20),
    total_plays INT,
    points_scored INT,
    points_allowed INT
);