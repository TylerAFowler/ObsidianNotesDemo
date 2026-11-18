-- Rows whose county code is not in the state county list (requirement CDL-REQ-001).
SELECT s.crash_id, s.county_code
FROM crash_stg.crash_2025 s
LEFT JOIN crash_rpt.county k ON k.county_code = s.county_code
WHERE k.county_code IS NULL
-- FIPS codes (54xxx) are accepted and mapped through crash_rpt.county_fips.
