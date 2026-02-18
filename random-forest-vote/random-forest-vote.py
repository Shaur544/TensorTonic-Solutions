import numpy as np

def random_forest_vote(predictions):

    predictions = np.array(predictions)
    T, N = predictions.shape

    final= []
    for i in range(N):
        votes= predictions[:, i]

        values, count = np.unique(votes, return_counts=True)
        max_count = count.max()

        candidates= values[count == max_count]

        final.append(int(candidates.min()))
    return final