# neo-location-tree
A Neo4j, ElasticSearch and Python location tree implementation 


To create a Location:

mutation {
 createLocation(name:"Argentina", locationId:3, parentId:1) {
   ok,
   detail
   location {
     id
     name
     locationId
   }
 }
}

To delete a Location: 

mutation {
 deleteLocation(locationId:1) {
   ok,
   detail
 }
}
