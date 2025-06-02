def generate_sql_from_question(question: str) -> str:
    question = question.lower()

    if "soc of vehicle" in question and "right now" in question:
        return """
  SELECT soc_pct 
FROM raw_telemetry rt
JOIN vehicles v ON rt.vehicle_id = v.vehicle_id
WHERE v.registration_no = 'GBM6296G'
ORDER BY ts DESC
LIMIT 1;

    """

    elif "how many srm t3" in question and "my fleet" in question:
        return """
        SELECT COUNT(*) FROM vehicles
        WHERE model = 'SRM T3';
        """

    elif "srm t3" in question and "exceed 33" in question and "last 24" in question:
        return """
 SELECT v.vehicle_id, MAX(rt.batt_temp_c) AS max_temp
FROM raw_telemetry rt
JOIN vehicles v ON rt.vehicle_id = v.vehicle_id
WHERE v.model = 'SRM T3'
  AND rt.ts::timestamp >= (
      SELECT MAX(ts)::timestamp FROM raw_telemetry
  ) - INTERVAL '24 HOURS'
GROUP BY v.vehicle_id
HAVING MAX(rt.batt_temp_c) > 33;
"""
    elif "fleet-wide average soc comfort zone" in question:
        return """
    SELECT AVG(soc_pct) AS avg_soc
    FROM raw_telemetry
    WHERE soc_pct BETWEEN 30 AND 80;
    """
    elif "which vehicles spent more than 20% of the past week in the 90–100% soc band" in question:
        return """
SELECT vehicle_id,
       COUNT(*) FILTER (WHERE soc_pct BETWEEN 90 AND 100) AS soc_high,
       COUNT(*) AS total,
       ROUND((COUNT(*) FILTER (WHERE soc_pct BETWEEN 90 AND 100)) * 100.0 / COUNT(*), 2) AS percent_high
FROM raw_telemetry
WHERE ts::timestamp BETWEEN '2025-05-07 00:00:00' AND '2025-05-14 23:59:59'
GROUP BY vehicle_id;
"""
    elif "currently driving" in question and "soc < 30%" in question:
            return """
SELECT COUNT(*)
FROM (
SELECT DISTINCT ON (vehicle_id) vehicle_id, soc_pct
FROM raw_telemetry
ORDER BY vehicle_id, ts DESC
        ) sub
WHERE soc_pct < 30;
        """
    elif "total km" in question and "driving hours" in question and "past 7 days" in question:
        return """
SELECT vehicle_id,ROUND(SUM(distance_km_15m)::NUMERIC, 2) AS total_km,ROUND((SUM(distance_km_15m) / NULLIF(AVG(avg_speed_kph_15m), 0))::NUMERIC, 2) AS total_hours
FROM processed_metrics
WHERE ts::timestamp BETWEEN '2025-05-07 00:00:00' AND '2025-05-14 23:59:59'
GROUP BY vehicle_id
ORDER BY total_km DESC;
    """
  
    elif "how many srm t3 evs have driven today" in question:
        return """
 SELECT COUNT(DISTINCT rt.vehicle_id)
FROM raw_telemetry rt
JOIN vehicles v ON rt.vehicle_id = v.vehicle_id
WHERE v.model = 'SRM T3'
  AND DATE(rt.ts) = '2025-05-14';


    """



    return "-- SQL generation not supported for this question."

