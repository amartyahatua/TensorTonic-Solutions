def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    topk = recommended[0:k]
    intersection = list(set(topk) & set(relevant))
    precision = len(intersection)/k 
    recall = len(intersection)/len(relevant)

    return [float(precision), float(recall)]