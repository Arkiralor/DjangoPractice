import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_v1.models import Score
from app_v1.serializers import ScoreSerializer, FileUploadSerializer

# Create your views here.

class BatchUploadView(APIView):
    '''
    API to batch upload scores via JSON file.
    '''
    serializer_class = FileUploadSerializer

    def post(self, request):
        '''
        POST request to upload JSON file.
        '''
        serialized_file = self.serializer_class(data=request.data)
        serialized_file.is_valid(raise_exception=True)
        
        file = serialized_file.validated_data['file']
        df = pd.read_json(file)
        df = df.to_dict(orient='records')

        for row in df:
            deserialized = ScoreSerializer(data=row)
            if deserialized.is_valid():
                deserialized.save()
            else:
                return Response(deserialized.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {
                "hits": df
            },
            status=status.HTTP_200_OK
        )


class ScoreView(APIView):
    '''
    API to get scores.
    '''
    def get(self, request):

        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):

        data = request.data

        if data.get('name') is None or data.get('score') is None or data.get('name') == "" or data.get('score') == "":
            return Response(
                {
                    "message": "Name and score are required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        deserialized = ScoreSerializer(data=data)
        deserialized.is_valid(raise_exception=True)
        deserialized.save()

        return Response(
            deserialized.data,
            status=status.HTTP_201_CREATED
        )


class GetRankedScoreView(APIView):
    '''
    API to get ranked scores.
    '''
    def get(self, request):
        rank = int(request.GET.get('rank'))

        if rank is None or rank == "":
            return Response(
                {
                    "message": "Rank is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        ranked_scores = Score.objects.all().order_by('-score').values_list('score', flat=True).distinct()
        if rank <= 0 or rank > len(ranked_scores):
            return Response(
                {
                    "message": "Rank is out of range"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        ranked_score = ranked_scores[rank-1]


        scorers = Score.objects.filter(score=ranked_score).values('name', 'score')

        serialized = ScoreSerializer(scorers, many=True)

        return Response(
            {
                "rank": rank,
                "score": ranked_score,
                "results": serialized.data,
            },
            status=status.HTTP_200_OK
        )
