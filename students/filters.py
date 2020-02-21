#filtering Student Deatils 

import django_filters

from .models import  StudentRegister

class Searchfilter(django_filters.FilterSet):

    class meta:
        model=StudentRegister
        fields= ('gender')