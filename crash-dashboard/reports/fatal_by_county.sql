SELECT k.county_name, COUNT(*) AS fatal_crashes, SUM(c.fatalities) AS fatalities
FROM crash_rpt.crash c JOIN crash_rpt.county k ON k.county_code = c.county_code
WHERE c.severity = 'K' AND EXTRACT(YEAR FROM c.crash_date) = 2025
GROUP BY k.county_name ORDER BY fatal_crashes DESC
