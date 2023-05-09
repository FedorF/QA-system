from typing import Dict

import numpy as np
import sklearn.metrics.pairwise as metrics


def find_answer(q: list, answer_emb: np.array, ind2answer: Dict[int, str]) -> str:
    """
    Arguments
    :param q: question embedding
    :param answer_emb: embedded answers database
    :param ind2answer: index to answer mapping
    :return: answer
    """
    q = np.array(q).reshape(1, -1)
    sim = 1 - np.arccos(metrics.cosine_similarity(q, answer_emb))/np.pi
    return ind2answer[np.argmax(sim)]
