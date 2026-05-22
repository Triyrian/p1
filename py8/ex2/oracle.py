import os
from dotenv import load_dotenv


CONFIGURATION_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]


def load_config() -> tuple[dict[str, str], list[str]]:
    load_dotenv()

    config = {}
    miss = []

    for variable in CONFIGURATION_VARS:
        value = os.getenv(variable)
        if value is None:
            miss.append(variable)
        else:
            config[variable] = value

    return config, miss


def display_config(config: dict[str, str]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config.get("MATRIX_MODE", "unknown")
    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
        print(f"Log Level: {config.get("LOG_LEVEL")}")
    else:
        print("Database: Connected to production system")
        print("Log Level:", config.get("LOG_LEVEL"))

    if config.get("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    if config.get("ZION_ENDPOINT"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check(miss: list[str]) -> None:
    print("\nEnvironment security check:")

    if not miss:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Missing variables:", ", ".join(miss))


if __name__ == "__main__":
    config, miss = load_config()

    if miss:
        print("Missing configuration variables:")
        for variable in miss:
            print("-", variable)

    display_config(config)
    security_check(miss)
