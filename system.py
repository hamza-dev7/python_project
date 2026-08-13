import random


class GymError(Exception):
    pass

class MemberNotFoundError(GymError):
    def __init__(self, member_id):
        super().__init__(f"Member '{member_id}' does not exist")

class DuplicateMemberError(GymError):
    def __init__(self, member_id):
        super().__init__(f"Member '{member_id}' does already exist")
    


class Gym:
    def __init__(self):
        self.members:dict = {}

    def add_member(self, member:object):
        if member.id in self.members:
            raise DuplicateMemberError(member.id)
        else:
            self.members[member.id] = member
            print(f"{member.id} added successfuly")
    
    def remove_member(self, member:object):
            self.members.pop(member.id)
            print(f"{member.id} removed successfuly")

    def id_search(self, member_id):
        if member_id not in self.members:
            raise MemberNotFoundError(member_id)
        else:
            return self.members[member_id]
    
    def name_search(self, first_name, last_name):
        for member in self.members.values():
            if member.first_name == first_name and member.last_name == last_name:
                return member


    class Membership:
        def __init__(self):
            self.membership_dict:dict = {
                                    "1": [], # 1 month
                                    "2": [], # 3 months
                                    "3": [], # 6 months
                                    "4": []  # 12 months
                                        }
        
        def add_membership(self,member:object, membership_type):
            self.membership_dict[membership_type].append(member.id)
            member.membership = membership_type
            print("added succesfuly")

        def remove_membership(self,member:object, membership_type):
            self.membership_dict[membership_type].remove(member.id)
            print("removed successfuly")




class Member:
    def __init__(self, first_name, last_name, id=None, membership=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id if id is not None else f"{random.randint(0, 999):03d}"
        self.membership = membership
        # self.is_paying = True

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)