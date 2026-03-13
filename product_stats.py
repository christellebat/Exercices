def total_products(products):

    return len(products)


def longest_name(products):

    return max(products, key=len)


def shortest_name(products):

    return min(products, key=len)


def average_name_length(products):

    lengths = [len(p) for p in products]

    return sum(lengths) / len(lengths)