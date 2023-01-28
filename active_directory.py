class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    """
    users = group.get_users()
    if user in users:
        return True

    for g in group.get_groups():
        r = is_user_in_group(user, g)
        if r:
            return True

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

if __name__ == "__main__":
    print(is_user_in_group("tony", child))
    print(is_user_in_group("sub_child_user", sub_child))
    print(is_user_in_group("sub_child_user", parent))
    print(is_user_in_group("sub_child_user", child))