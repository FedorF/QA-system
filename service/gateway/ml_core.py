from typing import Dict

import numpy as np
import sklearn.metrics.pairwise as metrics


def find_cluster(q: list, db: np.array) -> int:
    """
    Arguments
    :param q: embedded question
    :param db: centroids database
    :param ind2cluster: index to cluster mapping
    :return: cluster
    """
    q = np.array(q).reshape(1, -1)
    sim = 1 - np.arccos(metrics.cosine_similarity(q, db))/np.pi
    cl_id = int(np.argmax(sim))
    return cl_id
