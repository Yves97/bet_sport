from django.http import Http404
from app_pari.models import Sport,Ligue
class Spot():
    sports = Sport.objects.all()
    """sports = [{'id':1,'nom':'football','taux_pari': '80%'},
              {'id':2,'nom':'basket','taux_pari': '15%'},
              {'id':3,'nom':'tenis','taux_pari': '40%'}
            ]"""
    @classmethod
    def all(cls):
        return cls.sports
    @classmethod
    def find(cls,id):
        try:
            return cls.sports[int(id) - 1]
        except:
            raise Http404('Erreur sur la page') 
class Ligue():
    ligue = Ligue.objects.all()
    
    @classmethod
    def all(cls):
        return cls.ligue
    @classmethod
    def found(cls,id):
        try:
            return cls.ligue[int(id) - 1 ]
        except:
            raise Http404('Erreur sur la page ligue')
