from django.shortcuts import render
from reviews.models import Review, Comment
from .forms import CommentForm, ReviewForm


def reviews_index(request):
    reviews = Review.objects.all().order_by('-created_on')
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews_index.html", context)

def review_create(request):
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = Review(
                project=review_form.cleaned_data["project"],
                title=review_form.cleaned_data["title"],
                author=review_form.cleaned_data["author"],
                body=review_form.cleaned_data["body"],
            )
            review.save()
            #return redirect('home')
    context = {
        'review_form': review_form
    }
    return render(request, "review_create.html", context=context)

def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    comments = Comment.objects.filter(review=review)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                review=review
            )
            comment.save()

    context = {
        "review": review,
        "comments": comments,
        "form": form,
    }

    return render(request, "review_detail.html", context)