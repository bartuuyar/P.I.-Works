df.groupby("country")['daily_vaccinations'].mean().sort_values(ascending=False)[0:3]
