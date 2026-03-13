class Book:

    def __init__(self, title, price, rating, stock):
        self.title = title
        self.price = price
        self.rating = rating
        self.stock = stock

    def __str__(self):
        return f"{self.title} - £{self.price} ({self.rating})"