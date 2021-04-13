from graphene import ObjectType, String, Schema, Field, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import Column, Integer, String

from database import db_session, Base
db = db_session.session_factory()


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    nr = Column(Integer)

class BlogSchema(SQLAlchemyObjectType):
    class Meta:
        model = Blog


class Query(ObjectType):

    all_blogs = List(BlogSchema)

    def resolve_all_blogs(self, info, id):
        print(id)
        query = BlogSchema.get_query(info)  # SQLAlchemy query
        return query.all()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/", GraphQLApp(schema=Schema(query=Query)))
