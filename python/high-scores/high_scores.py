def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    ordered_scores = sorted(scores, reverse=True)
    return ordered_scores[:3]



