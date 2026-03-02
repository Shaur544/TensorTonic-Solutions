def k_means_assignment(points, centroids):
    assi=[]
    for p in points:
        best_dist = float('inf')
        best_idx= 0
        for j in range(len(centroids)):
            c = centroids[j]

            # Compute squared Euclidean distance
            dist = 0
            for d in range(len(p)):
                dist += (p[d] - c[d]) ** 2

            # Use strict < for tie-breaking
            if dist < best_dist:
                best_dist = dist
                best_idx = j

        assi.append(best_idx)

    return assi