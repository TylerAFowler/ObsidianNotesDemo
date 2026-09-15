SELECT county_name, COUNT(*) AS crashes,
       SUM(CASE WHEN severity = 'K' THEN 1 ELSE 0 END) AS fatal
FROM crash_rpt.crash c JOIN crash_rpt.county k ON k.county_code = c.county_code
WHERE EXTRACT(YEAR FROM c.crash_date) = :year
GROUP BY county_name ORDER BY crashes DESC
