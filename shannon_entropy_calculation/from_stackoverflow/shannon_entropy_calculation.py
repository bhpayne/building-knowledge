# reproducing http://www.shannonentropy.netmark.pl/

# H(x) = -\sum_{i=1}^n p(x_i) \log_b p(x_i)

# from http://codereview.stackexchange.com/questions/85879/functions-and-a-gui-for-entropy-related-calculations

"""Utilities for entropy-related calculations."""


from math import ceil as _ceil, log2 as _log2


def prob_to_info(probability):
    """Converts probability in the range from 0 to 1 into information measured
    in bits, therefore using the dual logarithm. Returns None if the probability
    is equal to zero."""
    if probability == 0:
        return None
    elif probability == 1:
        return 0
    else:
        return -_log2(probability)


def info_to_prob(information):
    """Converts information measured in bits to probablity."""
    return 2**-information


def entropy(iterable):
    """Calculates the Shannon entropy of the given iterable."""
    return sum(prob[1]*prob_to_info(prob[1]) for prob in char_mapping(iterable))


def optimal_bits(iterable):
    """Calculates the optimal usage of bits for decoding the iterable."""
    return _ceil(entropy(iterable)) * len(iterable)


def metric_entropy(iterable):
    """Calculates the metric entropy of the iterable."""
    return entropy(iterable) / len(iterable)


def char_mapping(iterable):
    """Creates a dictionary of the unique chararacters and their probability
    in the given iterable."""
    char_map = dict.fromkeys(set(iterable))
    for char in set(iterable):
        probability = iterable.count(char) / len(iterable)
        char_map[char] = probability

    return sorted(char_map.items(), key=lambda x: x[1], reverse=True)