from collections import deque

def is_non_terminal(char):
    return char.isupper()

def parse_grammar():
    print("\nEnter productions one by one.")
    print("Example:")
    print("S -> aB | bA")
    print("A -> a | aS | bAA")
    print("B -> b | bS | aBB")
    print("\nType DONE when finished.\n")

    grammar = {}

    while True:
        line = input("Production: ").strip()

        if line.upper() == "DONE":
            break

        if "->" not in line:
            print("Invalid production.")
            print("Use format: S -> aB | bA")
            continue

        left, right = line.split("->", 1)

        left = left.strip()
        right = right.strip()

        if len(left) != 1 or not left.isupper():
            print(
                "Left side must be one uppercase "
                "non-terminal."
            )
            continue

        productions = [
            p.strip()
            for p in right.split("|")
        ]

        grammar.setdefault(left, [])

        for production in productions:
            if production not in grammar[left]:
                grammar[left].append(production)

    return grammar

def terminal_count(string):
    return sum(
        1
        for char in string
        if not is_non_terminal(char)
    )

def possible_state(current, target):
    if terminal_count(current) > len(target):
        return False

    return True

def find_leftmost_derivation(
    grammar,
    start,
    target
):
    queue = deque()

    queue.append(
        (start, [start])
    )

    visited = {start}

    max_length = max(
        len(target) + 5,
        20
    )

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        position = -1

        for i, char in enumerate(current):
            if is_non_terminal(char):
                position = i
                break

        if position == -1:
            continue

        non_terminal = current[position]

        if non_terminal not in grammar:
            continue

        for production in grammar[non_terminal]:
            new_string = (
                current[:position]
                + production
                + current[position + 1:]
            )

            if len(new_string) > max_length:
                continue

            if not possible_state(
                new_string,
                target
            ):
                continue

            if new_string in visited:
                continue

            visited.add(new_string)

            queue.append(
                (
                    new_string,
                    path + [new_string]
                )
            )

    return None

def find_rightmost_derivation(
    grammar,
    start,
    target
):
    queue = deque()

    queue.append(
        (start, [start])
    )

    visited = {start}

    max_length = max(
        len(target) + 5,
        20
    )

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        position = -1

        for i in range(
            len(current) - 1,
            -1,
            -1
        ):
            if is_non_terminal(current[i]):
                position = i
                break

        if position == -1:
            continue

        non_terminal = current[position]

        if non_terminal not in grammar:
            continue

        for production in grammar[non_terminal]:
            new_string = (
                current[:position]
                + production
                + current[position + 1:]
            )

            if len(new_string) > max_length:
                continue

            if not possible_state(
                new_string,
                target
            ):
                continue

            if new_string in visited:
                continue

            visited.add(new_string)

            queue.append(
                (
                    new_string,
                    path + [new_string]
                )
            )

    return None

def find_used_production(
    previous,
    current,
    leftmost=True
):
    positions = []

    for i, char in enumerate(previous):
        if is_non_terminal(char):
            positions.append(i)

    if not positions:
        return None, None

    if leftmost:
        position = positions[0]
    else:
        position = positions[-1]

    non_terminal = previous[position]

    prefix = previous[:position]
    suffix = previous[position + 1:]

    if not current.startswith(prefix):
        return None, None

    if suffix:
        if not current.endswith(suffix):
            return None, None

        replacement = current[
            len(prefix):
            len(current) - len(suffix)
        ]
    else:
        replacement = current[
            len(prefix):
        ]

    return non_terminal, replacement

def print_derivation(
    path,
    title,
    leftmost=True
):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    if path is None:
        print("No derivation found.")
        return

    print(path[0])

    for i in range(1, len(path)):
        previous = path[i - 1]
        current = path[i]

        nt, replacement = find_used_production(
            previous,
            current,
            leftmost
        )

        if nt is not None:
            print(
                f"   -> {current}"
                f"    ({nt} -> {replacement})"
            )
        else:
            print(
                f"   -> {current}"
            )

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

def build_leftmost_tree(path):

    if not path:
        return None

    root = Node(path[0][0])

    current_nodes = [root]

    for next_string in path[1:]:

        position = None

        for i, node in enumerate(current_nodes):
            if is_non_terminal(node.value):
                position = i
                break

        if position is None:
            break

        node = current_nodes[position]

        current_string = "".join(
            n.value
            for n in current_nodes
        )

        prefix = current_string[:position]
        suffix = current_string[position + 1:]

        if not next_string.startswith(prefix):
            continue

        if suffix:

            if not next_string.endswith(suffix):
                continue

            replacement = next_string[
                len(prefix):
                len(next_string) - len(suffix)
            ]

        else:
            replacement = next_string[
                len(prefix):
            ]

        children = []

        for char in replacement:
            child = Node(char)
            children.append(child)

        node.children = children

        current_nodes = (
            current_nodes[:position]
            + children
            + current_nodes[position + 1:]
        )

    return root

def print_tree(
    node,
    prefix="",
    is_last=True,
    root=True
):
    if root:
        print(node.value)
    else:
        connector = (
            "└── "
            if is_last
            else "├── "
        )

        print(
            prefix
            + connector
            + node.value
        )

    if not node.children:
        return

    if root:
        new_prefix = ""
    else:
        new_prefix = (
            prefix
            + ("    " if is_last else "│   ")
        )

    for i, child in enumerate(node.children):

        last = (
            i == len(node.children) - 1
        )

        print_tree(
            child,
            new_prefix,
            last,
            False
        )

def main():

    print("=" * 70)
    print("       CONTEXT FREE GRAMMAR DERIVATION TOOL")
    print("=" * 70)

    print("\nRules:")
    print("• Uppercase letters = Non-terminals")
    print("• Everything else = Terminal")
    print("• Numbers are terminals")
    print("• Special characters are terminals")

    grammar = parse_grammar()

    if not grammar:
        print("\nNo productions entered.")
        return

    print("\nYour Grammar:")
    print("-" * 40)

    for nt, productions in grammar.items():
        print(
            f"{nt} -> "
            + " | ".join(productions)
        )

    start = input(
        "\nEnter start symbol [default S]: "
    ).strip()

    if not start:
        start = "S"

    target = input(
        "Enter string to derive: "
    ).strip()

    print("\nSearching for derivations...")

    left_path = find_leftmost_derivation(
        grammar,
        start,
        target
    )

    right_path = find_rightmost_derivation(
        grammar,
        start,
        target
    )

    print("\n" + "=" * 70)
    print("RESULT")
    print("=" * 70)

    if left_path is None and right_path is None:
        print(
            f'\nThe string "{target}" '
            "cannot be derived from the given productions."
        )
        return

    print(
        f'\nThe string "{target}" '
        "CAN be derived from the given productions."
    )

    if left_path:
        print_derivation(
            left_path,
            "LEFTMOST DERIVATION",
            leftmost=True
        )
    else:
        print(
            "\nNo leftmost derivation found."
        )

    if right_path:
        print_derivation(
            right_path,
            "RIGHTMOST DERIVATION",
            leftmost=False
        )
    else:
        print(
            "\nNo rightmost derivation found."
        )

    if left_path:
        print("\n" + "=" * 70)
        print("DERIVATION TREE")
        print("=" * 70)

        tree = build_leftmost_tree(
            left_path
        )

        print_tree(tree)

    print("\n" + "=" * 70)
    print("DONE")
    print("=" * 70)

if __name__ == "__main__":
    main()
