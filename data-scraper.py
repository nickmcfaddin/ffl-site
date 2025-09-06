# IMPORTS ----------------------------------------------------------------------
import nfl_data_py as nfl
import matplotlib.pyplot as plt
import os

# Load desired seaons to dataframe(can alter the 'years' variable)
years = list(range(2022, 2023))
df = nfl.import_seasonal_data(years)

# Filter for runningbacks using thresholds
df = df[(df['carries'] >= 50) & (df['attempts'] <= 20)]

# Not wanting to compare fantasy points to itself. Take out all useless metrics to measure
exclude_cols = ['fantasy_points', 'fantasy_points_ppr', 'season', 'player_id']
stats_to_compare = [col for col in df.select_dtypes(include='number').columns if col not in exclude_cols]

# Create folders for plots -> expandable for standard and half-ppr. Then loop through them
output_folders = {'full_ppr': 'plots_full_ppr'}

for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

scoring_types = {'full_ppr': 'fantasy_points_ppr'}

# for each type of scoring - standard, half, full ppr (in this case just full ppr)
for scoring_name, scoring_col in scoring_types.items():
    
    # Calculate correlations for all stats only keeping the ones that have some relevance
    correlations = {}
    for stat in stats_to_compare:
        corr = df[stat].corr(df[scoring_col])
        if corr > 0:
            correlations[stat] = corr

    # Get our top 10
    top_stats = sorted(correlations, key = correlations.get, reverse = True)[:10]
    print(f"\nTop 10 correlated stats for {scoring_name} scoring format:")
    for stat in top_stats:
        print(f"{stat}: {correlations[stat]:.3f}")
    
    # for each of the top 10 stats, we will print a scatterplot
    for stat in top_stats:
        for year in years:

            # only include players from this specific year using .copy() so we don't accidentally modify the df
            df_year = df[df['season'] == year].copy()

            # Get our x and y value for this specific stat per player to plot
            df_year['fantasy_rank'] = df_year[scoring_col].rank(ascending = False)
            df_year['stat_rank'] = df_year[stat].rank(ascending = False)

            # Plot
            plt.figure(figsize=(6, 6))
            plt.scatter(df_year['stat_rank'], df_year['fantasy_rank'])
            plt.xlabel(f'{stat.replace("_", " ").title()} Rank')
            plt.ylabel('Fantasy Points Rank')
            plt.title(f'{scoring_name.upper()} - {stat} vs Fantasy Rank ({year})')
            plt.grid(alpha = 0.3)

            # Save plot
            filename = f"{stat}_{year}.png"
            plt.savefig(os.path.join(output_folders[scoring_name], filename))
            plt.close()

print("Top 10 plots generated and saved!")

