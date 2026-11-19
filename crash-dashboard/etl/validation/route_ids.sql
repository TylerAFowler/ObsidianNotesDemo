-- Route IDs that LRS v2 does not know about (checked against the nightly LRS snapshot).
SELECT s.crash_id, s.route_id
FROM crash_stg.crash_2025 s
WHERE s.route_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM lrs.route_v2 r WHERE r.route_id = s.route_id)
