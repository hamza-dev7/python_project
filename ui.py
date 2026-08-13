import os

import data
import system


class UI:
    def __init__(self):
        self.gym = system.Gym()
        self.membership = system.Gym.Membership()
        self.member = system.Member
        

    @staticmethod
    def decoration1():
        print("=" * 32)
    @staticmethod
    def decoration2():
        print("-" * 32)
    
    @staticmethod
    def input_decoration():
        print("-" * 4, end="")
    
    @staticmethod
    def clear():
        os.system("clear")

    def ui_add_member(self):
        try:
            self.decoration1()
            self.input_decoration()
            first_name = input("Enter first name: ")
            self.input_decoration()
            last_name = input("Enter last name: ")
            self.decoration1()
            if self.gym.name_search(first_name, last_name):
                member = self.gym.name_search(first_name, last_name)
            else:
                member = self.member(first_name, last_name)
            self.gym.add_member(member)
        except system.GymError as e:
            print(e)
            return
        
    def ui_remove_member(self, member:object):
        try:
            self.gym.remove_member(member)
        except system.GymError as e:
            print(e)
            return

    def show_memberships(self):
        self.decoration1()
        self.decoration2()
        print("1- 1 month \n2- 3 months \n3- 6 months \n4- 12 months")
        self.decoration2()
        self.decoration1()

    def ui_add_membership(self, member:object):
        try:
            self.show_memberships()
            self.decoration1()
            self.input_decoration()
            membership_type = input("Enter membership type: ")
            self.decoration1()
            self.membership.add_membership(member, membership_type)
        except system.GymError as e:
            print(e)
            return
    
    def ui_change_membership(self, member:object):
        try:
            self.show_memberships()
            self.decoration1()
            self.input_decoration()
            membership_type = input("Enter membership type: ")
            self.decoration1()
            self.membership.remove_membership(member, member.membership)
            self.membership.add_membership(member, membership_type)
        except system.GymError as e:
            print(e)
            return

    def show_mem_info(self, member:object):
        while True:
            self.clear()
            self.decoration1()
            print(f"Name: {member.first_name} {member.last_name}")
            print(f"ID: {member.id}")
            print(f"Membership: {member.membership}")
            self.decoration1()
            self.decoration2()
            print("1-Add membership \n2-Change membership \n3-Remove member \n4-Back")
            self.decoration2()
            self.decoration1()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.ui_add_membership(member)
                continue
            elif choice == "2":
                self.ui_change_membership(member)
                continue
            elif choice == "3":
                self.ui_remove_member(member)
                break
            elif choice == "4":
                break

    def show_all_members(self):
        while True:
            self.clear()
            if not self.gym.members:
                self.decoration2()
                print("No registered members")
                self.decoration2()
                choice = input("Enter any key to return: ")
                if choice:
                    break
            else:
                for member in self.gym.members.values():
                    self.decoration1()
                    print(f"Name: {member.first_name} {member.last_name}")
                    print(f"ID: {member.id}")
                self.decoration1()
                self.decoration2()
                print("1-id search \n2-Back")
                self.decoration2()
                self.decoration1()
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.ui_id_search()
                    continue
                elif choice == "2":
                    break

    def ui_id_search(self):
        try:
            self.decoration1()
            member_id = input("Enter member id: ")
            member = self.gym.id_search(member_id)
            self.show_mem_info(member)
        except system.GymError as e:
            print(e)
            return
        



    
ui = UI()
gym_members_file = "python_project/gym_members.json" 
raw_data = data.load_json(gym_members_file)
for key, value in raw_data.items():
    ui.gym.members[key] = ui.member.from_dict(value)
while True:
    ui.clear()

    UI.decoration1()
    UI.decoration2()
    print("1-Add member \n2-show all members \n3-Search member \n4-Exit")
    UI.decoration2()
    UI.decoration1()

    choice = input("Enter your choice: ")
    if choice == "1":
        ui.ui_add_member()
        continue
    elif choice == "2":
        ui.show_all_members()
        continue
    elif choice == "3":
        ui.ui_id_search()
        continue
    elif choice == "4":
        optimized_data = {member.id: member.to_dict() for member in ui.gym.members.values()}
        data.save_json(gym_members_file, optimized_data)
        break
    else:
        print("Invalid choice")
        continue