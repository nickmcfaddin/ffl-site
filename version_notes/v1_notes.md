# Version 1 Objective

Figure out what statistics matter the most in a runningbacks fantasy football production.

## Hypothesis
Touches (carries, and receptions) will matter the most. Additionally within targets I believe that the type of target will be impactful. For a runningback, getting a first look target vs a checkdown where it was a bail out for the quarterback is significant. This indicates that the runningback receptions are incorporated into the scheme/gameplan rather than a last resort option.

## Dependencies

```
pip install nfl_data_py 
```

## Procedure
Based on the data available, we weren't able to get in to some of the more in depth metrics such as adot (average depth of target), type of target, etc. Using what we had we plotted each eligible runningback's fantasy rank in ppr scoring that year against each type of stat. Any statistic that had a linear upward trend indicated that there was some relevant correlation between that type of stat and the RB's fantasy production.

Obviously, there were some stats that were going to be very irrelevant such as sacks, fumbles and passing yards, but the overall process was the same per statistic. I ended up weeding out the irrelevant metrics by using a correlation function to get the top 10 correlated metrics based on their comparison with fantasy rank in ppr scoring. Once I did this, I only plotted the scatterplots of those top 10 to see how they matched against each other.

## Results
Ended up with a folder of scatterplots for the 2022 season with the top 10 metrics contributing to runningback fantasy football output in ppr scoring indicating each RB's fantasy performance vs the selected metric.

The metrics with their associated correlations were as follows
1. carries: 0.844
2. rushing_yards: 0.841
3. ppr_sh: 0.836
4. rushing_first_downs: 0.818
5. target_share: 0.802
6. wopr_x: 0.787
7. receiving_yards_after_catch: 0.785
8. targets: 0.783
9. receiving_yards: 0.778
10. receptions: 0.774

This was interesting as part of my hypothesis was correct, but it turns out that there is actually more that matters than just how many times a runningback touches the ball.

Carries was still the most important of the metrics, along with rushing yards which makes sense as that directly exemplifies what a runningback does with their carries and how much they can produce.

2 metrics stood out to me that I hadn't ever really considered. ppr_sh, which is the share of ppr points relative to their teammates. This makes a lot of sense as there are only so many mouths to feed on an offense, but not a statistic that I would have thought about. Additonally, wopr_x which is the weighted measure of rushing and receiving opportunities relative to the team total of opportunities. Both of these statistics help to incorporate how much of their teams workload they get. It won't always be applicable to do a 1v1 comparison of touches (carries and receptions) as players on different teams have different competition on their team for touches, different defenses that impact what type of game situations they are in, as well as scheme. These team based statistics help to take some of the variability out of those direct comparisons.
<br><br>

<div align="center">

![RB Weighted Measure of Rushing and Receiving Opportunities Relative to Team vs PPR Rank](plots_full_ppr/wopr_x_2022.png)

*Figure: Scatterplot of RB Weighted Measure of Rushing and Receiving Opportunities Relative to Team vs PPR Rank*

</div>

<br><br>

## Next Steps

The next steps would be to use this, along with another version to incorporate college statistics (in order to include rookies) to thus create a machine learning prediction model that will update every year to predict which runningbacks will score the most points. 

Additional factors that I will want to include are their strength of schedules, coach/coordinator (and any changes), age and injury history. I believe that if I can limit it to about 15 metrics, that I could get a fairly accurate model that may be able to out project standard models such as ESPN, Yahoo and Sleeper.


