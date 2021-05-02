from pony import orm
from . import DB


class Users(DB.Entity):
    email = orm.PrimaryKey(str)
    password_hash = orm.Required(bytes)
    groups = orm.Required(str, default="user")

    @staticmethod
    def create(**kwargs):
        return Users(**kwargs)

    def dictify(self):
        return {
            'email': self.email,
            'groups': self.group(),
        }

    def group(self):
        return ['anybody'] + self.groups.split()
