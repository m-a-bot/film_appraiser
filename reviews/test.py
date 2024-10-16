from models import ReviewModel

def main():
	review = ReviewModel("some text")

	print(review.rating)
	print(review.sentiment)

if __name__ == "__main__":
	main()
