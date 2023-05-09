from typing import Dict

import numpy as np
import pandas as pd

import config


def read_ans2vec(path: str) -> Dict[str, np.array]:
    return pd.read_pickle(path)


def load_answer_emb(ans2vec: Dict[str, np.array]) -> np.array:
    ind = np.zeros((len(ans2vec.values()), 512))
    for i, vec in enumerate(ans2vec.values()):
        ind[i] = vec
    return ind


def load_ind2answer(ans2vec: Dict[str, np.array]) -> Dict[int, str]:
    ind2answer = {}
    for i, answer in enumerate(ans2vec.keys()):
        ind2answer[i] = answer
    return ind2answer


ans2vec = read_ans2vec(config.ANSWER_EMBED_PATH)
ind2answer = load_ind2answer(ans2vec)
answer_emb = load_answer_emb(ans2vec)
del ans2vec
