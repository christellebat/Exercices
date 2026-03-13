def price_stats(books):

    prices = [b.price for b in books]

    return {
        "average": round(sum(prices) / len(prices), 2),
        "min": min(prices),
        "max": max(prices)
    }


def rating_distribution(books):

    ratings = {}

    for b in books:
        ratings[b.rating] = ratings.get(b.rating, 0) + 1

    return ratings


def global_stats(books):

    return {
        "total_books": len(books),
        "price_stats": price_stats(books),
        "ratings": rating_distribution(books)
    }