from django.db.models import Manager
from django.db.models.query import QuerySet

from query import Calculation            

class CalculationQuerySet(QuerySet):
    """Queryset that exposes a 'calculate' method to do database level calculations"""
    def calculate(self, **kwargs):
        return self.complex_filter(Calculation(**kwargs))


class CalculationManager(Manager):
    """Manager that uses the Calculation QuerySet, with a calculate method."""
    def get_query_set(self):
        return CalculationQuerySet(self.model)
    
    def calculate(self, **kwargs):
        return self.get_query_set().calculate(**kwargs)
