#!/usr/bin/python

from _string import formatter_field_name_split
from string import Formatter

class DFormatter(Formatter):
     def get_value(self, field_name, args, kwargs):
         return getattr(kwargs, field_name)

     def get_field(self, field_name, args, kwargs):
         first, rest = formatter_field_name_split(field_name) 
         obj = self.get_value(first, args, kwargs) 

         for is_attr, i in rest:
             if is_attr:
                 obj = getattr(obj, i)
             else:
                 obj = obj[i]
         return obj, first

