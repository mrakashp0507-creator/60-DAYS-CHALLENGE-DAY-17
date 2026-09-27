def generate_subsets(gems):

    result = []
    current = []

    def backtrack(index):

        # Base case:
        # We have considered every gem
        if index == len(gems):
            result.append(current.copy())
            return

        
        backtrack(index + 1)

        # -----------------------------------------
        # Decision 2: TAKE the gem
        # -----------------------------------------

        current.append(gems[index])

        backtrack(index + 1)

        # -----------------------------------------
        # Undo the decision
        # -----------------------------------------

        current.pop()

    backtrack(0)

    return result


# -------------------------------------------------
# Display Decision Tree
# -------------------------------------------------

def show_tree(gems, index=0, current=None, indent=""):

    if current is None:
        current = []

    if index == len(gems):
        print(indent + "→ " + str(current))
        return

    # Do not take
    print(indent + f"Skip {gems[index]}")
    show_tree(
        gems,
        index + 1,
        current,
        indent + "    "
    )

    # Take
    current.append(gems[index])

    print(indent + f"Take {gems[index]}")
    show_tree(
        gems,
        index + 1,
        current,
        indent + "    "
    )

    current.pop()


# -------------------------------------------------
# Main Program
# -------------------------------------------------

print("=" * 60)
print("        💎 MAGICAL TREASURE CHEST")
print("        Backtracking Subset Generator")
print("=" * 60)

input_gems = input(
    "\nEnter gems separated by spaces: "
)

gems = input_gems.split()


# Generate subsets
subsets = generate_subsets(gems)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("\n--- ALL POSSIBLE COMBINATIONS ---")

for number, subset in enumerate(subsets, start=1):

    if len(subset) == 0:
        print(number, ":", "[]")
    else:
        print(number, ":", subset)


# -------------------------------------------------
# Count
# -------------------------------------------------

print("\n--- RESULT ---")

print("Number of gems:", len(gems))

print("Total combinations:", len(subsets))

print(
    "Expected combinations:",
    2 ** len(gems)
)


# -------------------------------------------------
# Decision Tree
# -------------------------------------------------

print("\n--- DECISION TREE ---")

show_tree(gems)

print("\n" + "=" * 60)
print("Treasure search completed!")
print("=" * 60)