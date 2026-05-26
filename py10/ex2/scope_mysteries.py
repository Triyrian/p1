from typing import Callable, Dict, Union


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def power_accumulation(adding: int) -> int:
        nonlocal initial_power
        initial_power += adding
        return initial_power

    return power_accumulation


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: Dict[str, int] = {}

    def store(key: str, value: int) -> Dict[str, int]:
        memory[key] = value
        return memory

    def recall(key: str) -> Union[int, str]:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")

    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    total_power = spell_accumulator(100)
    print(f"Base 100, add 20: {total_power(20)}")
    print(f"Base 100, add 30: {total_power(30)}")

    print("\nTesting enchantment factory...")
    flame_enchantment = enchantment_factory("Flaming")
    print(flame_enchantment("Sword"))
    frozen_enchantment = enchantment_factory("Frozen")
    print(frozen_enchantment("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
