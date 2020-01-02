from BlogDBmodels.models import *


def create_user(name, email):
    Base.metadata.create_all(engine)
    user = User(nickname=name, email=email)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(user)
    session.commit()


def create_post(title, text, user_email):
    Base.metadata.create_all(engine)
    post = Post(title=title, text=text, user_email=user_email)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(post)
    session.commit()


def create_tag(tag_name):
    Base.metadata.create_all(engine)
    tag = Tag(tag_name=tag_name)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(tag)
    session.commit()
    return tag
