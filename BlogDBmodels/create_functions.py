from models import User, Tag, Post, Base, engine
from sqlalchemy.orm import sessionmaker


def session_add(param):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(param)
    session.commit()


def create_user(name, email):
    user = User(nickname=name, email=email)
    session_add(user)


def create_post(title, text, user_email):
    post = Post(title=title, text=text, user_email=user_email)
    session_add(post)


def create_tag(tag_name):
    tag = Tag(tag_name=tag_name)
    session_add(tag)
