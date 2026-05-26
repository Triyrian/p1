from functools import wraps
from typing import Callable, Any
import time
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        t0 = time.time()
        res = func(*args, **kwargs)
        time.sleep(0.1)
        t1 = time.time()

        duration = t1 - t0
        print(f"Spell completed in {duration:.3f} seconds")
        return res

    return timer


@spell_timer
def heal() -> str:
    return "Heal restores some HP"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = None

            if args and isinstance(args[0], int):
                power = args[0]
            elif len(args) >= 3:
                power = args[2]
            else:
                power = kwargs.get("power")

            if power is None or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


@power_validator(10)
def fireball(power: int, target: str) -> str:
    return f"Fireball inflict {power} HP to {target}"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )

            return ("Spell failed unexpectedly")

        return wrapper

    return decorator


@retry_spell(3)
def unlucky_spell() -> str:
    rval = random.random()
    if rval < 0.7:
        raise ValueError("Spell fizzled")
    return "Waaaaaaagh spelled!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(f"Result: {heal()}")

    print("\nTesting power validator")
    print(fireball(15, "Dragon"))
    print(fireball(5, "Dragon"))

    print("\nTesting retrying spell...")
    print(unlucky_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Nom"))
    print(MageGuild.validate_mage_name("N0m"))
    guild = MageGuild()
    print(guild.cast_spell("Fireball", 15))
    print(guild.cast_spell("Fireball", 5))
