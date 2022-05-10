from django.urls import path
from app_v1.apis import BatchUploadView, ScoreView, GetRankedScoreView

urlpatterns = [
    path('scores/all', ScoreView.as_view(), name='get_or_add_scores'),
    path('scores/upload', BatchUploadView.as_view(), name='add_scores_from_file'),
    path('scores/ranked', GetRankedScoreView.as_view(), name='get_ranked_scores'),
]
