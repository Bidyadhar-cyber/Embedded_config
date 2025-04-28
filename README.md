Embedded Config:-
      Embedded Config is a Python package that provides essential functionalities for Raspberry Pi GPIO control and system information.
It includes modules for:

GPIO Input Setup

GPIO Output Setup

Serial Communication 

Raspberry Pi Information 

Features:-
📥 Read sensor data using GPIO input.

📤 Control actuators/LEDs using GPIO output.

🔍 Fetch Raspberry Pi information.

Installation:-
Recommended: Install inside a virtual environment.

# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Clone or copy the package, then inside the folder:
pip install .
If you really need system-wide installation (⚠️ Not recommended):

pip install . --break-system-packages
