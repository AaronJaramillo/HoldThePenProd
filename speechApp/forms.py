#-*- coding: utf-8 -*-
from django import forms

class searchBar(forms.Form):
   searchString = forms.CharField(max_length = 100)