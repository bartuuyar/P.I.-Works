import pandas as pd
df = pd.read_csv("country_vaccination_stats.csv")

country_min = df.groupby('country')['daily_vaccinations'].transform('min')
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(country_min)
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)
