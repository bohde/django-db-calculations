# Django DB Calculations

## What

This is a way for doing calculations in the database, and having them magically appear as attributes on your models. 

## Why

Django's [extra](http://docs.djangoproject.com/en/dev/ref/models/querysets/#extra) isn't DRY. 

## Usage
  
You'll need Django 1.2. Add the custom manager to your model, like so

    from django.db import models
    from db_calculations import CalculationManager

    class MyModel(models.Model):
        ...
        objects = CalculationManager()


Now you can use the calculate method, using the builtin F objects to build your expression    

## Example

    >>> from basic.models import Number
    >>> from django.models import F
    >>> Number.objects.create(x=2, y=3)
    >>> Number.objects.calculate(z=F('x')+F('y'))[0].z
    ... 5.0

    >>> Number.objects.calculate(z=F('x')-F('y'))[0].z
    ... -1.0

    >>> Number.objects.calculate(z=F('x')*F('y'))[0].z
    ... 6.0

    >>> Number.objects.calculate(z=F('x')/F('y'))[0].z
    ... 0.66666666666666663

    >>> Number.objects.calculate(z=F('x')+F('y')).calculate(z_squared=F('z')*F('z'))[0].z_squared
    ... 25.0


## Warning

The current state is more of a proof of concept than any sort of thing you might want to use for your project. It pretty much won't work outside of basic operations. In fact, it will go pretty crazy once you start to do anything fancy.
