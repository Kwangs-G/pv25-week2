from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QGroupBox,
    QMessageBox
)

import sys

class KwangReg(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Week 2 : Layout - user Registration Form")
        self.setGeometry(200, 200, 420, 420)

        main_layout = QVBoxLayout()

        identitas_group = self.identitas()
        main_layout.addWidget(identitas_group)

        nav_layout = self.navigation()
        main_layout.addLayout(nav_layout)

        # Registration Form
        regis_group = self.registrasi()
        main_layout.addWidget(regis_group)

        action_layout = self.button()
        main_layout.addLayout(action_layout)

        self.setLayout(main_layout)

    def identitas(self):
        group = QGroupBox("Identitas")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nama  : Nama_Anda"))
        layout.addWidget(QLabel("NIM   : Nim_anda"))
        layout.addWidget(QLabel("Kelas : Kelas_Anda"))
        group.setLayout(layout)
        return group

    def navigation(self):
        layout = QHBoxLayout()
        for name in ["Home", "Profile", "Settings"]:
            layout.addWidget(QPushButton(name))
        return layout

    def registrasi(self):
        group = QGroupBox("Form Registrasi")
        layout = QVBoxLayout()

        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()

        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)

        self.country = QComboBox()
        self.country.addItems(["Pilih Negara", "Indonesia", "America", "Cina", "DLL"])

        layout.addWidget(QLabel("Nama Lengkap:"))
        layout.addWidget(self.full_name)

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email)

        layout.addWidget(QLabel("Nomor HP:"))
        layout.addWidget(self.phone)

        layout.addWidget(QLabel("Jenis Kelamin:"))
        layout.addLayout(gender_layout)

        layout.addWidget(QLabel("Negara:"))
        layout.addWidget(self.country)

        group.setLayout(layout)
        return group

    def button(self):
        layout = QHBoxLayout()
        self.submit_button = QPushButton("Submit")
        self.cancel_button = QPushButton("Cancel")

        self.submit_button.clicked.connect(self.submit_form)
        self.cancel_button.clicked.connect(self.clear_form)

        layout.addWidget(self.submit_button)
        layout.addWidget(self.cancel_button)
        return layout

    def submit_form(self):
        name = self.full_name.text()
        email = self.email.text()
        phone = self.phone.text()
        gender = "Male" if self.gender_male.isChecked() else "Female" if self.gender_female.isChecked() else "Not Selected"
        country = self.country.currentText()

        if not name or not email or not phone or country == "Pilih Negara":
            QMessageBox.warning(self, "Input Error", "Harap lengkapi semua data dengan benar.")
            return

        QMessageBox.information(self, "Data : ",
                                f"Nama: {name}\nEmail: {email}\nHP: {phone}\nGender: {gender}\nNegara: {country}")

    def clear_form(self):
        self.full_name.clear()
        self.email.clear()
        self.phone.clear()
        self.gender_male.setChecked(False)
        self.gender_female.setChecked(False)
        self.country.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KwangReg()
    window.show()
    sys.exit(app.exec())