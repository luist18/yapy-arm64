def sorensen_dice_coefficient(lhs, rhs):
    similarity_score = 0
    max_score = 0

    for element in lhs:
        max_score += lhs[element]
        if element in rhs:
            similarity_score += min(lhs[element], rhs[element])

    for element in rhs:
        max_score += rhs[element]

    if max_score == 0:
        return 0

    return similarity_score * 2 / max_score
