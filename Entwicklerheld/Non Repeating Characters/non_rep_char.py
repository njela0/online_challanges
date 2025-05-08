def find_first_non_repeated_char(sequence: str):

    first_non_repeated_char = ""

    if not sequence:
        first_non_repeated_char = None

    else:
        for index, char in enumerate(sequence):
            count_char = sequence.lower().count(char.lower())

            if count_char == 1:
                first_non_repeated_char = char
                break
            elif count_char > 1:
                if index < len(sequence) - 1:
                    continue
                else:
                    first_non_repeated_char = None
                    break

    return first_non_repeated_char

seq1 = "Entwicklerheld"
seq2 = "abcabc"
seq3 = ""

print(find_first_non_repeated_char(seq1))