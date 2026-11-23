SELECT 'county' AS check_name, COUNT(*) AS failures FROM (@county_codes.sql)
UNION ALL
SELECT 'route', COUNT(*) FROM (@route_ids.sql)
