Программа-иммитация блога с использованием SQLAlchemy

Внутри проекта 3 файла: models.py, create_functions.py и run.py

Models.py - создаются классы моделей для блога: User, Post, Tag, а также промежуточная таблица tags_posts_table которая связывает между собой таблицы с постами и тегами

User - модель пользователя с уникальным id именем и email
```python
//python code
    class User(Base):
      __tablename__ = 'users'

      id = Column(Integer, primary_key=True)
      nickname = Column(String, nullable=False)
      email = Column(String, nullable=False)

      posts = relationship("Post", back_populates="user")

      def __repr__(self):
          return "<User: id = {}, nickname= {}, email= {}>".format(self.id, self.nickname, self.email)
```

Post - модель поста с уникальным id, датой создания, названием, текстом, пользовательским email'ом и датой обновления. Добавлена связь с 
таблицей user и таблицей tags через secondary таблицу tags_posts_table
```python
//python code
    class Post(Base):
      __tablename__ = 'posts'
      id = Column(Integer, primary_key=True)
      created_date = Column(DateTime, default=datetime.datetime.utcnow)
      title = Column(String, nullable=False)
      text = Column(String, nullable=False)
      user_email = Column(Integer, ForeignKey('users.email'))
      on_update = Column(DateTime, default=datetime.datetime.utcnow)
      is_published = Column(Boolean, default=False)

      user = relationship("User", back_populates="posts")
      tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")

      def __repr__(self):
          return "<Post: date = {}, title= {}, text= {}>".format(self.created_date, self.title, self.text)
```
Tag - модель тега с уникальным id, названием и связью с таблицей posts через secondary таблицу tags_posts_table

```python
//python code
    class Tag(Base):
      __tablename__ = 'tags'
      id = Column(Integer, primary_key=True)
      tag_name = Column(String, nullable=False)

      posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")

      def __repr__(self):
          return "<Tag: {}>".format(self.tag_name)
```

Файл create_functions.py содержит функции по созданию и добавлению в БД объектов моделей User, Post и Tag

```python
//python code
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
```

Файл run.py содержит логику работы программы имитирующую взаимодействие с блогом
- Добавить пользователья в БД
- Добавить пост в БД
- Добавить тег в БД
- Вывод всех пользователей из БД
- Вывод всех постов из БД
- вывод всех тегов из БД
- Поиск постов по email пользователя
- Поиск всех постов по тегам
