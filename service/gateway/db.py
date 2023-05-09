import numpy as np 
import pandas as pd 

import config


def load_centroids(path: str) -> np.array:
    centroids = np.zeros((4, 512))
    for cl_id, vec in pd.read_pickle(path).items():
        if cl_id in config.VALID_CLUSTER_ID:
            centroids[int(cl_id)] = vec
    return centroids

centroids = load_centroids(config.CENTROIDS_PATH)
