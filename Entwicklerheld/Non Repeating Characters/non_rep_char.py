def find_first_non_repeated_char(sequence: str):

    first_non_repeated_char = ""

    for char in sequence:
        count_char = sequence.lower().count(char.lower())

        if not sequence:
            return None

        elif count_char == 1:
            print(f"first non-repeated character: {char}")

            first_non_repeated_char = char
            return first_non_repeated_char


seq1 = "Entwicklerheld"
seq2 = "abcabc"
seq3 = ""

print(find_first_non_repeated_char(seq1))