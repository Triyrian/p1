from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)

    if operation == "multiply":
        return reduce(operator.mul, spells)

    if operation == "max":
        return max(spells)

    if operation == "min":
        return min(spells)

    raise ValueError(f"Error - Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "thunder": partial(base_enchantment, 50, "thunder"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(x: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @dispatch.register
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @dispatch.register
    def _(x: list) -> str:
        return f"Multi-cast: {len(x)} spells"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} {target} inflicts {power} HP"


if __name__ == "__main__":
    spell_powers = [5, 12, 3]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    try:
        print(f"Unknown: {spell_reducer(spell_powers, 'oiad')}")
    except ValueError as exc:
        print(exc)

    print("\nTesting partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants["thunder"]("Sword"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "ice", "heal"]))
