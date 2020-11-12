import graphene
import api.schema
import users.schema


class Query(users.schema.Query, api.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, api.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)