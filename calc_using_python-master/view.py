from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QApplication


class GUI(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 300)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplayLED()
        self._createButtons()

    def _createDisplayLED(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   'Bin to Dec': (4, 0),
                   'Dec to Bin': (4, 1),
                   'Bin to Oct': (4, 2),
                   'Oct to Bin': (4, 3),
                   'Bin to Hex': (4, 4),
                   'Hex to Bin': (5, 0),
                  }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
      
        self.generalLayout.addLayout(buttonsLayout)

       
        self.buttons['Bin to Dec'].clicked.connect(self.bin_to_dec)
        self.buttons['Dec to Bin'].clicked.connect(self.dec_to_bin)
        self.buttons['Bin to Oct'].clicked.connect(self.bin_to_oct)
        self.buttons['Oct to Bin'].clicked.connect(self.oct_to_bin)
        self.buttons['Bin to Hex'].clicked.connect(self.bin_to_hex)
        self.buttons['Hex to Bin'].clicked.connect(self.hex_to_bin)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

    def bin_to_dec(self):
        """Convert binary to decimal."""
        binary = self.getDisplayText()
        decimal = str(int(binary, 2))
        self.setDisplayText(decimal)

    def dec_to_bin(self):
        """Convert decimal to binary."""
        decimal = self.getDisplayText()
        binary = bin(int(decimal))[2:]
        self.setDisplayText(binary)

    def bin_to_oct(self):
        """Convert binary to octal."""
        binary = self.getDisplayText()
        octal = oct(int(binary, 2))[2:]
        self.setDisplayText(octal)

    def oct_to_bin(self):
        """Convert octal to binary."""
        octal = self.getDisplayText()
        binary = bin(int(octal, 8))[2:]
        self.setDisplayText(binary)

    def bin_to_hex(self):
        """Convert binary to hexadecimal."""
        binary = self.getDisplayText()
        hexadecimal = hex(int(binary, 2))[2:]
        self.setDisplayText(hexadecimal)

    def hex_to_bin(self):
        """Convert hexadecimal to binary."""
        hexadecimal = self.getDisplayText()
        binary = bin(int(hexadecimal, 16))[2:]
        self.setDisplayText(binary)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = GUI()
    calc.show()
    sys.exit(app.exec_())