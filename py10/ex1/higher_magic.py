from typing import Tuple, Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return f"Mega {base_spell(target, power * multiplier)}"
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(target: str, power: int) -> str:
        if condition(target):
            return spell(target, power)
        return "Spell fizzled"
    return (casted)


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> List[str]:
        all_spell: List[str] = []
        for spell in spells:
            all_spell.append(spell(target, power))
        return all_spell
    return sequence


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def condition_wizard(target: str) -> bool:
    return target != "Wizard"


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))

    print("\nTesting power amplifier...")
    megaheal = power_amplifier(heal, 2)
    print(
        f"Original: {heal('Knight', 10)}, "
        f"Amplified: {megaheal('Dragon', 10)}"
    )

    print("\nTesting conditional caster...")
    cast_conditional = conditional_caster(condition_wizard, fireball)
    print(cast_conditional("Dragon", 10))

    print("\nTesting spell sequence...")
    spell_list = [heal, fireball, megaheal]
    sequence = spell_sequence(spell_list)
    print(sequence("Goblin", 5))
