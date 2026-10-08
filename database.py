import sqlite3
import os

DATABASE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "travel_planner.db"
)


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                destination TEXT NOT NULL,
                days INTEGER NOT NULL,
                travelers INTEGER NOT NULL,
                budget TEXT,
                interests TEXT,
                food TEXT,
                transport TEXT,
                trip_plan TEXT NOT NULL
            )
        """)


def save_trip(
    destination,
    days,
    travelers,
    budget,
    interests,
    food,
    transport,
    trip_plan
):
    create_database()

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO trips (
                destination,
                days,
                travelers,
                budget,
                interests,
                food,
                transport,
                trip_plan
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            destination,
            days,
            travelers,
            budget,
            interests,
            food,
            transport,
            trip_plan
        ))


def get_saved_trips():
    create_database()

    with get_connection() as connection:
        trips = connection.execute("""
            SELECT
                id,
                destination,
                days,
                travelers,
                budget,
                interests,
                food,
                transport,
                trip_plan
            FROM trips
            ORDER BY id DESC
        """).fetchall()

    return trips


create_database()

