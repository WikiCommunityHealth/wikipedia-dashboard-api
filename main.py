from graphene import ObjectType, String, Schema, Field, List
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from graphene.relay import Node

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp

from mongoengine import Document
from mongoengine.fields import (DateTimeField, ReferenceField, StringField, IntField)
from mongoengine import connect


connect(host='mongodb://root:example@localhost:27017/test?authSource=admin')

class KevinModel(Document):
    meta = {'collection': 'pippo'}
    name = StringField(required=True)

class Kevin(MongoengineObjectType):

    class Meta:
        model = KevinModel
        interfaces = (Node,)

class Query(ObjectType):
    node = Node.Field()
    kevins = MongoengineConnectionField(Kevin)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/", GraphQLApp(schema=Schema(query=Query, types=[Kevin])))
