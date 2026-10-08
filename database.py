import sqlite3

DATABASE_NAME = "travel_planner.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
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

    connection.commit()
    connection.close()


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
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
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

    connection.commit()
    connection.close()
def get_saved_trips():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
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
    """)

    trips = cursor.fetchall()

    connection.close()

    return trips