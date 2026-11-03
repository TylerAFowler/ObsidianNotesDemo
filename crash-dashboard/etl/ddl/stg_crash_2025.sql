CREATE TABLE crash_stg.crash_2025 (
  crash_id      VARCHAR2(20) PRIMARY KEY,
  crash_date    DATE NOT NULL,
  county_code   VARCHAR2(3),
  route_id      VARCHAR2(20),
  milepost      NUMBER(7,3),
  severity      CHAR(1),
  latitude      NUMBER(9,6),
  longitude     NUMBER(9,6)
);
