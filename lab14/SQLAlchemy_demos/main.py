from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Base, User


class UserManager:
    def __init__(self) -> None:
        # Create an engine
        self.engine = create_engine('sqlite:///mydatabase.db')
        # self.engine = create_engine('mysql+pymysql://test:test1234@localhost/users_db', echo=True)

        # Create a session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_table(self):
        # Create the tables in the database
        Base.metadata.create_all(self.engine)

    def reflect_tables(self):
        # Reflect the database schema
        metadata = MetaData()
        metadata.reflect(bind=self.engine)

        # Print all tables in db
        for table in metadata.tables.values():
            print(table.name)

        # Retrieve a table
        users_table = metadata.tables['user']

        # Get table columns
        print(users_table.columns)

    def add_users(self, data):
        for user in data:
            # Create a new user instance
            new_user = User(
                name=user['name'],
                age=user['age'],

            )
            # Add the new user to the session
            self.session.add(new_user)

        # Commit the session to persist the changes
        self.session.commit()
        print('Data entered!')

    def get_all_users(self):
        # Query all users
        uesrs = self.session.query(User).all()
        for user in users:
            print(f'{user.name}, {user.age}')

    def get_user(self, id):
        user = self.session.query(User).filter_by(id=id).one()
        print(user.name)
        return user

    def update_user(self, id, user_data ):
        user = self.get_user(id=1)
        user.name=user_data['name']
        # Commit the session to persist the changes
        self.session.commit()

    def delete_user(self, id):
        self.session.query(User).filter_by(id=id).delete()
        # Commit the session to persist the changes
        self.session.commit()

if __name__ == '__main__':
    user_manager = UserManager()
    # user_manager.reflect_tables()
    user_manager.create_table()

    data = [
        {"name": "Ivan", "age": 30, "country":"Bulgaria", "town": "Sofie", "zip": 1504},
        {"name": "Mariya", "age": 25, "country":"Bulgaria", "town": "Sofie", "zip": 1504},
        {"name": "Petar", "age": 35, "country":"Bulgaria", "town": "Sofie", "zip": 1504}
    ]

    user_manager.add_users(data)
    # user_manager.get_all_users()

    # # user_manager.get_user(5)
    # # new_user_data = {
    # #     'name': 'Asen',
    # #     'age': 23
    # # }
    # # user_manager.update_user(id=3, user_data=new_user_data)


    # user_manager.delete_user(id=1)
    print('END')

