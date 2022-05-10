from app_v1.models import Score

def drop_all():
    Score.objects.all().delete()

if __name__=="__main__":
    drop_all()