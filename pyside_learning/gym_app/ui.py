from calendar import firstweekday
from mimetypes import init
import sys

import system
from data import GYM_MEM_FILE, MEMBERSHIP_DICT_FILE, load_json, save_json
from PySide6 import QtCore, QtGui, QtWidgets

class MyGym:
    def __init__(self):
        self.gym = system.Gym()
        # self.member = system.Member

    @QtCore.Slot()
    def add_member(self, first_name, last_name):
        member = system.Member(first_name, last_name)
        self.gym.add_member(member)


class AddMemberWindow(QtWidgets.QWidget):
    def __init__(self, my_gym: MyGym, parent=None):
        super().__init__(parent)
        self.my_gym = my_gym

        self.setWindowTitle("Add Member")

        self.fname_input = QtWidgets.QLineEdit()
        self.lname_input = QtWidgets.QLineEdit()

        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.addRow("First Name:", self.fname_input)
        self.form_layout.addRow("Last Name:", self.lname_input)

        self.save_btn = QtWidgets.QPushButton("Add Member")
        self.save_btn.clicked.connect(self.save)

        self.save_msg = QtWidgets.QLabel()


        self.box_layout = QtWidgets.QVBoxLayout()
        self.box_layout.addLayout(self.form_layout)
        self.box_layout.addWidget(self.save_btn)
        self.box_layout.addWidget(self.save_msg)
        self.box_layout.addStretch()
        self.setLayout(self.box_layout)

    def save(self):
        first_name = self.fname_input.text()
        last_name = self.lname_input.text()
        self.my_gym.add_member(first_name, last_name)
        member_id = list(self.my_gym.gym.members.keys())[-1]
        self.save_msg.setText(f"Member {first_name} {last_name} with ID:{member_id} added successfully!")
        self.fname_input.clear()
        self.lname_input.clear()


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Gym Management")


        self.title = QtWidgets.QLabel("      Gym Fitness      ")
        self.add = QtWidgets.QPushButton("Add Member")
        self.members = QtWidgets.QPushButton("Show Members")
        self.id_search = QtWidgets.QPushButton("Id Search Member")

        column = QtWidgets.QVBoxLayout()
        column.addWidget(self.title)
        column.addSpacing(20)
        column.addWidget(self.add)
        column.addWidget(self.members)
        column.addWidget(self.id_search)

        container = QtWidgets.QWidget()
        container.setLayout(column)
        container.setMaximumWidth(380)

        outer = QtWidgets.QHBoxLayout(self)
        outer.addStretch(1)
        outer.addWidget(container)
        outer.addStretch(1)

        self.setStyleSheet("""
            QLabel {
                font-size: 30px;
            }
            QPushButton{
                font-size: 16px;
                padding: 16px;
            }
        """)


app = QtWidgets.QApplication(sys.argv)
my_gym = MyGym()
window = MainWindow()
window.show()
app.exec()
optimized_data = {member.id: member.to_dict() for member in my_gym.gym.members.values()}
save_json(GYM_MEM_FILE, optimized_data)
