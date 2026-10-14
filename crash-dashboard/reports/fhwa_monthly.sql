-- Monthly FHWA extract: every crash reported in the previous month, one row per vehicle.
SELECT c.crash_id, c.crash_date, c.county_code, c.route_id, c.milepost, c.severity,
       v.vehicle_no, v.body_type, v.contributing_factor
FROM crash_rpt.crash c JOIN crash_rpt.vehicle v ON v.crash_id = c.crash_id
WHERE c.report_date >= ADD_MONTHS(TRUNC(SYSDATE, 'MM'), -1)
  AND c.report_date <  TRUNC(SYSDATE, 'MM')
ORDER BY c.crash_id, v.vehicle_no
