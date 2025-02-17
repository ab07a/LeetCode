from collections import Counter

def numTilePossibilities( tiles):
    seen = set()

    # Sort characters to handle duplicates efficiently
    sorted_tiles = "".join(sorted(tiles))

    # Find all unique sequences and their permutations
    return _generate_sequences(sorted_tiles, "", 0, seen) - 1
def _factorial( n):
    if n <= 1:
        return 1

    result = 1
    for num in range(2, n + 1):
        result *= num
    return result

def _count_permutations( seq):
    # Calculate permutations using factorial formula
    total = _factorial(len(seq))

    # Divide by factorial of each character's frequency
    for count in Counter(seq).values():
        total //= _factorial(count)

    return total

def _generate_sequences(
     tiles, current, pos, seen
):
    if pos >= len(tiles):
        # If new sequence found, count its unique permutations
        if current not in seen:
            seen.add(current)
            return _count_permutations(current)
        return 0

    # Try including and excluding current character
    return _generate_sequences(
        tiles, current, pos + 1, seen
    ) + _generate_sequences(tiles, current + tiles[pos], pos + 1, seen)

print(numTilePossibilities("AAB"))