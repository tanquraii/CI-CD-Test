import graphene
from . import models
from graphene_django import DjangoObjectType

class CatUserType(DjangoObjectType):
    class Meta:
        model = models.CatUser
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(CatUserType)
    def all_users_resolve(root,info):
        return models.CatUser.objects.all()

schema = graphene.Schema(query=Query)
