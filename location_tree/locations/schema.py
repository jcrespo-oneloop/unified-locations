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
    all_locations = DjangoFilterConnectionField(LocationType)
    location = graphene.relay.Node.Field(LocationType)

class CreateLocation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)
        location_id = graphene.Int(required = True)
        parent_id = graphene.Int(required = True)

    ok = graphene.Boolean()
    location = graphene.Field(LocationType)
    detail = graphene.String()

    def mutate(self, info, name, location_id, parent_id):
        try:
            Location.nodes.get(location_id = location_id)
            location = None
            ok = False
            detail = f"The location with id = {location_id} already exists"
        except:
            location = Location(
                name = name,
                location_id = location_id
            )
            parent = Location.nodes.get(location_id = parent_id)
            location.save()
            location.parent.connect(parent)
            ok = True
            detail = ""
            
        return CreateLocation(location=location, ok = ok, detail = detail)

class DeleteLocation(graphene.Mutation):
    class Arguments:
        location_id = graphene.Int(required = True)
        
    ok = graphene.Boolean()
    detail = graphene.String()
    
    def mutate(self, info, location_id):
        location = Location.nodes.get(location_id = location_id)
        if len(Location.nodes.has(parent = location).all()) == 0:
            location.delete()
            ok = True
            detail = ""
        else:
            ok = False
            detail = "The location has children, it can't be deleted"
            
        return DeleteLocation(ok = ok, detail = detail)
            

class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()
    delete_location = DeleteLocation.Field()
