from os import system
from time import sleep

system("cls")

ADJACENTS = ((-1 - 1j), (0 - 1j), (1 - 1j), (-1 + 0j), (1 + 0j), (-1 + 1j), (0 + 1j), (1 + 1j))


def print_animation(step, flashes, part_one):
    a = (
        ["\033c"]
        + list(
            "    "
            + "".join(
                str(octopuses[x + 1j * y] if octopuses[x + 1j * y] != 0 else f"\033[92m{octopuses[x + 1j * y]}\033[0m")
                for x in range(len(input[0]))
            )
            for y in range(len(input))
        )
        + ["\n"]
    )
    a[1] += f"    \033[93mstep: {step}\033[0m"
    a[3] += f"    \033[93mtotal flashes: {flashes}\033[0m"
    a[5] += f"    \033[96manswer part one: {part_one if part_one else ''}\033[0m"
    a[7] += f"    \033[36manswer part two: {step if all(v == 0 for v in octopuses.values()) else '' }\033[0m"
    print("\n".join(a))
    if step < 20:
        sleep(1 - 0.9 * (step - 1) / 20)
    else:
        sleep(0.1)


def compute_step():
    new_flashes = set()
    for k in octopuses:
        octopuses[k] += 1
        if octopuses[k] > 9:
            octopuses[k] = 0
            new_flashes.add(k)

    while new_flashes:
        for k in new_flashes:
            if octopuses[k] == 0:
                for adj in ADJACENTS:
                    if k + adj in octopuses and octopuses[k + adj] > 0:
                        octopuses[k + adj] += 1

        new_flashes = set()
        for k in octopuses:
            if octopuses[k] > 9:
                octopuses[k] = 0
                new_flashes.add(k)


def compute():
    flashes = 0
    step = 1
    part_one = None
    while True:
        compute_step()
        flashes += sum(1 for v in octopuses.values() if v == 0)
        print_animation(step, flashes, part_one)
        if step == 100:
            part_one = flashes
        if all(v == 0 for v in octopuses.values()):
            break
        step += 1

    return flashes


input = tuple(tuple(map(int, line)) for line in open("input").read().splitlines())
octopuses = {(x + 1j * y): input[y][x] for y in range(len(input)) for x in range(len(input[0]))}
compute()
