import pandas as pd
from sqlalchemy import create_engine

# Replace with your correct username (and password if any)
engine = create_engine("postgresql://senthilkumarshreeyasen@localhost:5432/fleetdb")

tables = [
    "fleets",
    "vehicles",
    "raw_telemetry",
    "processed_metrics",
    "charging_sessions",
    "trips",
    "alerts",
    "battery_cycles",
    "maintenance_logs",
    "drivers",
    "driver_trip_map",
    "geofence_events",
    "fleet_daily_summary"
]

for table in tables:
    file_path = f"data/{table}.csv"
    print(f"📥 Loading {file_path} into {table}...")

    try:
        df = pd.read_csv(file_path)
        df.to_sql(table, con=engine, if_exists='replace', index=False)
        print(f"✅ Successfully loaded {table}")
    except Exception as e:
        print(f"❌ Failed to load {table}: {e}")
