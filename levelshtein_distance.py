def levenshtein_distance(token1, token2):
    length_token1 = len(token1)
    length_token2 = len(token2)

    distances = [[0] * (length_token2 + 1) for _ in range(length_token1 + 1)]

    for t1 in range(length_token1 + 1):
        distances[t1][0] = t1

    for t2 in range(length_token2 + 1):
        distances[0][t2] = t2

    for t1 in range(1, length_token1 + 1):
        for t2 in range(1, length_token2 + 1):
            cost = 0 if token1[t1 - 1] == token2[t2 - 1] else 1

            distances[t1][t2] = min(
                distances[t1 - 1][t2] + 1,      # Deletion
                distances[t1][t2 - 1] + 1,      # Insertion
                distances[t1 - 1][t2 - 1] + cost  # Substitution
            )

    return distances[length_token1][length_token2]
