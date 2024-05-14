CREATE TEMPORARY TABLE median_daily_vaccinations AS
SELECT
    country,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS median_daily_vaccinations
FROM
    mytable
GROUP BY
    country;

CREATE TEMPORARY TABLE merged_table AS
SELECT
    t.*,
    m.median_daily_vaccinations
FROM
    mytable t
JOIN
    median_daily_vaccinations m
ON
    t.country = m.country;

UPDATE merged_table
SET daily_vaccinations = median_daily_vaccinations
WHERE daily_vaccinations IS NULL;

DROP TEMPORARY TABLE median_daily_vaccinations;
