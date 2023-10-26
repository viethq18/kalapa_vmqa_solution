
def litm_reordering(documents):
    """Los in the middle reorder: the most relevant will be at the
    middle of the list and more relevant elements at beginning / end.
    See: https://arxiv.org/abs//2307.03172"""

    tmp_documents = list(reversed(documents))
    reordered_result = []
    for i, value in enumerate(tmp_documents):
        if i % 2 == 1:
            reordered_result.append(value)
        else:
            reordered_result.insert(0, value)
    return reordered_result
