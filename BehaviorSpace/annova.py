import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

density = [10, 20, 30, 40, 50]

for d in density:
    headers = [
        "mosquito_infect_humans_mean",
        "mosquito_infect_humans_std",
        "humans_infect_mosquito_mean",
        "humans_infect_mosquito_std",
        "total_mosquitoes_mean",
        "total_mosquitoes_std",
        "mosquito_death_toll_mean",
        "mosquito_death_toll_std",
        "cur_human_population_mean",
        "cur_human_population_std",
        "infected_humans_percentage_mean",
        "infected_humans_percentage_std",
        "recovered_humans_percentage_mean",
        "recovered_humans_percentage_std",
        "total_larvae_mean",
        "total_larvae_std",
        "total_hatched_larvae_mean",
        "total_hatched_larvae_std"
    ]

    df = pd.read_csv(f"density_{d}.csv", header=None, names=headers)
    df.drop(index=df.index[:2], axis="index", inplace=True)
    df = df.apply(pd.to_numeric, errors='coerce')  # ensure everything is numeric
    model = ols('mosquito_infect_humans_mean ~ total_larvae_mean + total_hatched_larvae_mean + total_mosquitoes_mean + cur_human_population_mean', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    anova_table.to_csv(f"anova_results_density_{d}.csv")
