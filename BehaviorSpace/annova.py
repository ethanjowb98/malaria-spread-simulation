import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

headers = [
    "mosquito infect humans (mean)",
    "mosquito infect humans (std)",
    "humans infect mosquito (mean)",
    "humans infect mosquito (std)",
    "total-mosquitoes (mean)",
    "total-mosquitoes (std)",
    "mosquito-death-toll (mean)",
    "mosquito-death-toll (std)",
    "cur-human-population (mean) ",
    "cur-human-population (std)",
    "infected-humans-percentage (mean)",
    "infected-humans-percentage (std)",
    "recovered-humans-percentage (mean)",
    "recovered-humans-percentage (std)",
    "total-larvae (mean)",
    "total-larvae (std)",
    "total-hatched-larvae (mean)",
    "total-hatched-larvae (std)"
]

df = pd.read_csv("./10/FinalProject Effect of Water Density on Dengue Spread (10 density)-stats.csv", header=None, names=headers)
df.drop(index=df.index[0], axis="index", inplace=True)
model = ols('infection_rate ~ C(water_density)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
