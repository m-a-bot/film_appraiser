from django.shortcuts import render
from .forms import ReviewForm
from .models import ReviewModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():

            review_text = form.cleaned_data['review_text']

            review = ReviewModel(review_text)

            return render(request, 'reviews/review_result.html', {
                'rating': review.rating,
                'sentiment': review.sentiment,
                'review_text': review.review_text
            })
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/submit_review.html', {'form': form})
