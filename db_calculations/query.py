from django.db.models.sql.expressions import SQLEvaluator
from django.db.models.sql.constants import LOOKUP_SEP

class CalculationEvaluator(SQLEvaluator):
    """An SQL Evaluator that masquerades as an aggregate"""
    is_summary = False
    is_computed = True
    is_ordinal = False
    
    def as_sql(self, qn, connection, **extra):
        statement, values = super(CalculationEvaluator, self).as_sql(qn, connection)
        return statement % tuple(values)


class Calculation(object):
    """An object to perform database level calculations"""
    def __init__(self, **kwargs):
        self.calcs = kwargs
    
    def add_to_query(self, query, used_aliases):
        # Add the model fields to the query so that calculating the
        # aggregate field is correct
        
        query.add_fields([f.name for f in query.get_meta().fields])

        for alias, calculation in self.calcs.iteritems():
            c = CalculationEvaluator(calculation, query)
            query.aggregates[alias] = c

