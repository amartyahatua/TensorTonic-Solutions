def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    intersection = list(set(recommended[0:k]) & set(relevant))
    precision = len(intersection)/k 
    recall = len(intersection)/len(relevant)

    return [float(precision), float(recall)]