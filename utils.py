import re
def keep_token_pattern(token, pattern='[a-zA-Z0-9]{3,}'):
    if isinstance(token, list):
        kept_token = [keep_token_pattern(tok, pattern) for tok in token]
        return kept_token

    found = re.findall(pattern, token)

    if found:
        return found[0]

    return ""

from copy import deepcopy

def chain(input_, operations):
    operations_copy = deepcopy(operations)
    for operation in operations_copy:
        current_func = operation["function"]
        del operation["function"]
        input_ = current_func(input_, **operation)

    if isinstance(input_, list):
        return [input_token for input_token in input_ if input_token]

    return input_