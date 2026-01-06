import numpy as np

def calculate_ece(confidences, true_labels, predicted_labels, num_bins=10):
    """
    Expected Calibration Error (ECE) using equal-width bins on [0, 1].
    confidences: 1D array-like of predicted confidence (e.g., max softmax prob)
    true_labels, predicted_labels: 1D array-like of same length
    """
    confidences = np.asarray(confidences, dtype=float)
    true_labels = np.asarray(true_labels)
    predicted_labels = np.asarray(predicted_labels)

    # Bin edges and assignment (bins: 0..num_bins-1)
    bin_edges = np.linspace(0.0, 1.0, num_bins + 1)
    bin_ids = np.digitize(confidences, bin_edges[1:-1], right=False)  # puts 1.0 in last bin

    correct = (predicted_labels == true_labels)
    ece = 0.0
    n = len(confidences)

    for b in range(num_bins):
        idx = (bin_ids == b)
        if np.any(idx):
            bin_acc = np.mean(correct[idx])
            bin_conf = np.mean(confidences[idx])
            ece += (np.sum(idx) / n) * np.abs(bin_acc - bin_conf)

    return float(ece)

def calculate_rmsce(confidences, true_labels, predicted_labels, num_bins=10):
    confidences = np.asarray(confidences)
    true_labels = np.asarray(true_labels)
    predicted_labels = np.asarray(predicted_labels)

    N = len(confidences)
    if N == 0:
        return np.nan

    bin_edges = np.linspace(0.0, 1.0, num_bins + 1)
    squared_error = 0.0

    for i in range(num_bins):
        left, right = bin_edges[i], bin_edges[i + 1]
        if i == num_bins - 1:
            idx = (confidences >= left) & (confidences <= right)
        else:
            idx = (confidences >= left) & (confidences < right)

        n_b = np.sum(idx)
        if n_b == 0:
            continue

        bin_accuracy = np.mean(predicted_labels[idx] == true_labels[idx])
        bin_confidence = np.mean(confidences[idx])
        gap = bin_accuracy - bin_confidence
        squared_error += (n_b / N) * (gap ** 2)

    return float(np.sqrt(squared_error))

def ece_from_bin_pairs(bin_acc, bin_conf, counts=None):
    bin_acc = np.asarray(bin_acc, dtype=float)
    bin_conf = np.asarray(bin_conf, dtype=float)
    assert bin_acc.shape == bin_conf.shape

    gaps = np.abs(bin_acc - bin_conf)
    if counts is None:
        return float(np.mean(gaps))

    counts = np.asarray(counts, dtype=float)
    assert counts.shape == gaps.shape
    w = counts / counts.sum()
    
    return float(np.sum(w * gaps))

def rmsce_from_bin_pairs(bin_acc, bin_conf, counts=None):
    bin_acc = np.asarray(bin_acc, dtype=float)
    bin_conf = np.asarray(bin_conf, dtype=float)
    assert bin_acc.shape == bin_conf.shape

    sq_gaps = (bin_acc - bin_conf) ** 2
    if counts is None:
        return float(np.sqrt(np.mean(sq_gaps)))

    counts = np.asarray(counts, dtype=float)
    assert counts.shape == sq_gaps.shape
    w = counts / counts.sum()
    return float(np.sqrt(np.sum(w * sq_gaps)))