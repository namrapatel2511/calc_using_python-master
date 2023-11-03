from functools import partial

ERROR_MSG = 'ERROR'

class Controller:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
       
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', 'Bin to Dec', 'Dec to Bin', 'Bin to Oct', 'Oct to Bin', 'Bin to Hex', 'Hex to Bin'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['Bin to Dec'].clicked.connect(self._bin_to_dec)
        self._view.buttons['Dec to Bin'].clicked.connect(self._dec_to_bin)
        self._view.buttons['Bin to Oct'].clicked.connect(self._bin_to_oct)
        self._view.buttons['Oct to Bin'].clicked.connect(self._oct_to_bin)
        self._view.buttons['Bin to Hex'].clicked.connect(self._bin_to_hex)
        self._view.buttons['Hex to Bin'].clicked.connect(self._hex_to_bin)

    def _bin_to_dec(self):
        """Convert binary to decimal."""
        binary = self._view.getDisplayText()
        decimal = str(int(binary, 2))
        self._view.setDisplayText(decimal)

    def _dec_to_bin(self):
        """Convert decimal to binary."""
        decimal = self._view.getDisplayText()
        binary = bin(int(decimal))[2:]
        self._view.setDisplayText(binary)

    def _bin_to_oct(self):
        """Convert binary to octal."""
        binary = self._view.getDisplayText()
        octal = oct(int(binary, 2))[2:]
        self._view.setDisplayText(octal)

    def _oct_to_bin(self):
        """Convert octal to binary."""
        octal = self._view.getDisplayText()
        binary = bin(int(octal, 8))[2:]
        self._view.setDisplayText(binary)

    def _bin_to_hex(self):
        """Convert binary to hexadecimal."""
        binary = self._view.getDisplayText()
        hexadecimal = hex(int(binary, 2))[2:]
        self._view.setDisplayText(hexadecimal)

    def _hex_to_bin(self):
        """Convert hexadecimal to binary."""
        hexadecimal = self._view.getDisplayText()
        binary = bin(int(hexadecimal, 16))[2:]
        self._view.setDisplayText(binary)