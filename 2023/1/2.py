
with open("./input.txt") as f:
    lines = f.readlines()

def sum_first_and_last(numbers: list[int]):
    return (numbers[0] * 10 + numbers[-1]) or 0

def notok(_: str, start: int) -> dict:
    return {
        "kind": "notok",
        "data": None,
        "i": start + 1,
    }


def parse_numeric(line: str, start: int) -> dict:
    if not line[start].isdigit():
        return notok(line, start)
    return {
        "kind": "int",
        "data": int(line[start]),
        "i": start + 1,
    }

def parse_named_numeric(line: str, start: int) -> dict:
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    chopped = line[start:]
    for i, num in enumerate(nums):
        if chopped.startswith(num):
            return {
                "kind": "int",
                "data": i,
                "i": start + 1 # len(num) 🤔
            }
    return notok(line, start)


def parse_token(line: str, start: int) -> dict:
    res = parse_numeric(line, start)
    if res["kind"] == "int":
        return res
    return parse_named_numeric(line, start)

def parse_line(line: str) -> list[int]:
    nums = []
    i = 0
    while i < len(line):
        res = parse_token(line, i)
        i = res["i"]
        if res["kind"] == "int":
            n = res["data"]
            nums.append(n)
    return nums

total = 0
for line in lines:
    parsed_line = parse_line(line)
    total += sum_first_and_last(parsed_line)

print(total)
