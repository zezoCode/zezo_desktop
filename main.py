import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# functions #
def make_main_window():
	app = QApplication(sys.argv)
	window = QWidget()

	# Texts Layouts #

	# User Name Input #
	User_name = QLineEdit()
	User_name.setFont(QFont("Arial" , 12))
	User_name.setAlignment(Qt.AlignLeft)
	# end #

	# Age Input #
	User_age = QLineEdit()
	User_age.setFont(QFont("Arial" , 12))
	User_age.setValidator(QIntValidator())
	# end #

	# Gender Changes #
	gender = QLineEdit()
	gender.textChanged.connect(input_gender_finished)
   	# end #

	# Password Input #
	User_password = QLineEdit()
	User_password.setFont(QFont("Arial" , 12))
	User_password.setEchoMode(QLineEdit.Password)
	# end #

	# Phone Input #
	User_phone_number = QLineEdit()
	User_phone_number.setFont(QFont("Arial" , 12))
	User_phone_number.setInputMask('+99_9999_99999999')
	# end #

	# Read Only #
	Text_read_only = QLineEdit("Welcome")
	Text_read_only.setReadOnly(True)
	# end #

	# Form Layout #
	main_form = QFormLayout()
	main_form.addRow("User Name : " , User_name)
	main_form.addRow("Age : " , User_age)
	main_form.addRow("Phone Number : " , User_phone_number)
	main_form.addRow("Text changed : " , gender)
	main_form.addRow("Password : " , User_password)
	main_form.addRow("Read Only : " , Text_read_only)
	# end #

	User_password.editingFinished.connect(enter_press)

	window.setLayout(main_form)
	window.setWindowTitle("PyQt5")
	window.show()
	sys.exit(app.exec_())
def process():
	if __name__ == "__main__":
		make_main_window()
def input_gender_finished():
	print("GOOD")
def enter_press():
	print("GOOD PASSWORD")
# end functions #

def main():
	process()

main()