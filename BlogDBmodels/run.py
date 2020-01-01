from BlogDBmodels.run import *

Session = sessionmaker(bind=engine)
session = Session()

while True:
    response = input('\n\nWhat to do:\n'
          'Add user(au) | Add post(ap) | Add tag (at) | Tag some post (tp)\n'
          'Show all users(su) | Show all posts(sp) | Show all tags(st)\n'
          'Find post by User(fpu) | Find posts by Tag(fpt) ')

    if response not in ('au', 'ap', 'at', 'tp', 'su', 'sp','st', 'fpu', 'fpt'):
        print('Wrong command. Reload app')
        exit()


    # Добавить нового пользователя
    elif response =='au':
        name = input('Enter user nickname: ')
        email = input('Enter user email: ')
        Base.metadata.create_all(engine)
        #проверка на наличие пользователей(Если пусто - создать первого)
        objects = session.query(User).first()
        if objects is None:
            create_user(name, email)
            print('Добавлен новый пользователь')
        else:
            #проверка на существование пользователя по email
            for email in session.query(User).filter_by(email = email):
                if email:
                    print('Error: User already exists!')
                    exit()

            create_user(name, email)
            print('Добавлен новый пользователь')


    # Добавить новый пост
    elif response == 'ap':
        title = input('Enter post title: ')
        text = input('Enter post text: ')
        user_email = input('Enter author email: ')
        Base.metadata.create_all(engine)
        for email in session.query(User).filter_by(email=user_email):
            if email:
                create_post(title, text, user_email)
                print('Добавлен новый пост: {} с тегами: {}'.format(title, post.tags))
                exit()

        response = input('There is no user with this email - create new user? y/n ')
        if response == 'y':
            name = input('Enter user nickname: ')
            create_user(name, user_email)
            create_post(title, text, user_email)
            print('New post with title: "{}" by new user "{}"'.format(title, name))
        else:
            exit()

    # Добавить новый тег в базу
    elif response == 'at':
        tag_name = input('Enter new TAG name: ')
        Base.metadata.create_all(engine)
        # проверка на наличие пользователей(Если пусто - создать первого)
        objects = session.query(Tag).first()
        if objects is None:
            create_tag(tag_name)
            print('New TAG was added')
        else:
            # проверка на существование tag в базе
            for tag_name in session.query(Tag).filter_by(tag_name=tag_name):
                if tag_name:
                    print('Error: TAG already exists!')
                    exit()

            create_tag(tag_name)
            print('New TAG was added')


    # Назначаем постам нужные теги
    elif response == 'tp':

        for post in session.query(Post).order_by(Post.id):
            print('\nPost id: {}, title : {}, text: {}, user_email: {}'.format(post.id, post.title, post.text, post.user_email))
        post_id = input('Choose post id which you want to tag: ')
        tag_name = input('Enter tags for this post, use , to split tag names: ')
        x = '123'
        p = session.query(Post).filter_by(id = post_id).first()
        p.tags.append(tag_name)
        session.commir()



    #Показать всех пользователей
    elif response == 'su':
        for user in session.query(User).order_by(User.id):
            print('\nUser id: {}, username: {}, email: {}'.format(user.id, user.nickname, user.email))

    # Показать все посты
    elif response == 'sp':
        for post in session.query(Post).order_by(Post.id):
            print('\nPost id: {}, title : {}, text: {}, user_email: {}'.format(post.id, post.title, post.text, post.user_email))

    # Показать все теги
    elif response == 'st':
       for tag in session.query(Tag).order_by(Tag.id):
           print('\nTag id: {}, tag_name : {}'.format(tag.id, tag.tag_name))


    # Показать посты по email пользователя
    elif response == 'fpu':
        email = input('Find posts by user email: ')
        for post in session.query(Post).filter_by(user_email = email):
            print('\nPost id: {}, title : {}, text: {}, user_email: {}'.format(post.id, post.title, post.text, post.user_email))

