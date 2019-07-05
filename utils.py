import re
import operator
from copy import deepcopy


def keep_token_pattern(token, pattern='[a-zA-Z0-9]{3,}'):
    if isinstance(token, list):
        kept_token = [keep_token_pattern(tok, pattern) for tok in token]
        return kept_token

    found = re.findall(pattern, token)

    if found:
        return found[0]

    return ""


def chain(input_, operations):
    operations_copy = deepcopy(operations)
    for operation in operations_copy:
        current_func = operation["function"]
        del operation["function"]
        input_ = current_func(input_, **operation)

    if isinstance(input_, list):
        return [input_token for input_token in input_ if input_token]

    return input_


def print_top_tokens(feature_names, word_counts, n_top=10):
    tdidf_counts = zip(feature_names, word_counts.sum(axis=0).tolist()[0])
    sorted_x = sorted(dict(tdidf_counts).items(), key = operator.itemgetter(1), reverse = True)

    if n_top:
        return sorted_x[: n_top]
    else:
        return sorted_x