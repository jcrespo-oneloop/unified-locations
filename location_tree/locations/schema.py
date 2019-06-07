from locations.models import Location
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        filter_fields = ['name']
        interfaces = (graphene.relay.Node, )

class Query(object):
    location = graphene.relay.Node.Field(LocationType)
    all_locations = DjangoFilterConnectionField(LocationType)

class CreateLocation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)
        parent_name = graphene.String(required = True)

    ok = graphene.Boolean()
    location = graphene.Field(LocationType)

    def mutate(self, info, name, parent_name):
        location = Location(
            name = name
        )
        parent = Location.nodes.get(name = parent_name)
        location.save()
        location.parent.connect(parent)
        ok = True
        return CreateLocation(location=location, ok = ok)

class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()

