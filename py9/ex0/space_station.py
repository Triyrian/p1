from pydantic import BaseModel, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")

    station1 = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.fromisoformat("2024-01-01T10:00:00"),
    )
    print(f"ID: {station1.station_id}")
    print(f"Name: {station1.name}")
    print(f"Crew: {station1.crew_size} people")
    print(f"Power: {station1.power_level}%")
    print(f"Oxygen: {station1.oxygen_level}%")
    print(
        "Status: Operational"
        if station1.is_operational
        else "Status: Not Operational"
    )
    print()
    print("========================================")

    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2024-01-01T10:00:00"),
        )
    except Exception as err:
        print("Expected validator error:")
        print(err)


if __name__ == "__main__":
    main()
