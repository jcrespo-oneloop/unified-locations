from django.db import models
import neomodel

# Create your models here.

class LocationRelationship(neomodel.StructuredRel):
    on_date = neomodel.DateProperty(default_now = True)

class Location(neomodel.StructuredNode):
    full_name = neomodel.StringProperty(required=True)
    parent = neomodel.RelationshipTo("Location", "IS_IN", neomodel.ZeroOrOne, model = LocationRelationship)

    def __str__(self):
        return self.full_name

