def total_results(products):
    return len(products)


def first_three(products):
    return products[:3]


def cheapest_product(products):
    return min(products, key=lambda x: x["price"])


def most_expensive_product(products):
    return max(products, key=lambda x: x["price"])