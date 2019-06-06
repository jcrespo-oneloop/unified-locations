from locations.models import Location
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class LocationType(DjangoObjectType):

    class Meta:
        model = Location
        interfaces = (graphene.relay.Node, )
        filter_fields = [
            'full_name',
        ]


class Query(object):
    location = graphene.relay.Node.Field(LocationType)
    all_locations = DjangoFilterConnectionField(LocationType)