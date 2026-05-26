def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    print("\nTesting artifact sorter...")
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    print("\nTesting power filter...")
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    print("\nTesting spell transformer...")
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    print("\nTesting mage_stats")
    maxp = max(mages, key=lambda x: x['power'])['power']
    minp = min(mages, key=lambda x: x['power'])['power']
    avgp = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        "max_power": maxp,
        "min_power": minp,
        "avg_power": avgp,
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Wind Cloak', 'power': 91},
        {'name': 'Ice Wand', 'power': 112},
        {'name': 'Water Chalice', 'power': 100}
    ]
    mages = [
        {'name': 'Ember', 'power': 84, 'element': 'fire'},
        {'name': 'Casey', 'power': 54, 'element': 'water'},
        {'name': 'Ember', 'power': 80, 'element': 'water'}
    ]
    spells = ['freeze', 'darkness', 'fireball', 'flash']

    sorted_art = artifact_sorter(artifacts)
    for i in range(len(sorted_art) - 1):
        curr = sorted_art[i]
        next_art = sorted_art[i + 1]
        print(
            f"{curr['name']} ({curr['power']} power) comes before "
            f"{next_art['name']} ({next_art['power']} power)"
        )
    print(power_filter(mages, 83))
    print(mage_stats(mages))
    transformed_spells = spell_transformer(spells)
    for s in transformed_spells:
        print(s, end=" ")
