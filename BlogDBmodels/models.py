import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

engine = create_engine('sqlite:///my_blog.db')
Base = declarative_base()

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

tags_posts_table = Table(
    'tags_posts',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True),
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return "<User: id = {}, nickname= {}, email= {}>".format(self.id, self.nickname, self.email)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    user_email = Column(Integer, ForeignKey('users.email'))
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_published = Column(Boolean, default=False)

    user = relationship("User", back_populates="posts")
    tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")

    def __repr__(self):
        return 'Post id: {}, created_at: {}, title : {}, text: {}, user_email: {} updated_at: {}'.format(self.id, self.created_date, self.title, self.text,
                                                                               self.user_email, self.on_update)

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String, nullable=False)

    posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")

    def __repr__(self):
        return "<Tag: {}>".format(self.tag_name)
