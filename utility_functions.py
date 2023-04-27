import numpy as np


# --- model validation ---


def reciprocal_rank(recom_list, next_item):
    """
    Function to measure the reciprocal rank.
    There is only one relevant item, which is the next item.
    Thus, the RR is 1 divided by the position of the next item in the list of recommendations.
    In the case that the item is part of the list, the MRR is 0.

    :param recom_list list: list of ordered recommendations containing item ID strings
    :param next_item str: ID of next item
    :return float: reciprocal rank
    """
    if next_item in recom_list:
        # convert to list in case of numpy arrays
        recom_list = list(recom_list)
        return 1 / (recom_list.index(next_item) + 1)
    else:
        return 0


def mean_reciprocal_rank(recom_lists, next_items):
    """
    Function to measure the mean reciprocal rank for multiple recommendation lists and next items.

    :param recom_lists list: list of lists or numpy array containing multiple recommendation lists
    :param next_item list: list of next items
    :return float: mean reciprocal rank
    """
    rr_vals = []
    for recom_list, next_item in zip(recom_lists, next_items):
        rr_vals.append(reciprocal_rank(recom_list, next_item))
    mrr = np.mean(rr_vals)
    return mrr, rr_vals
