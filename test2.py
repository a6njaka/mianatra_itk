import sys
import lib_addition_3ch_hor  # Ensure this library is correctly installed and imported

# List all imported modules
imported_modules = list(sys.modules.keys())

for lib in imported_modules:
    print(lib)

# Check if "lib_addition_3ch_hor" is in the imported modules
if "lib_addition_3ch_hor" in sys.modules:
    # Retrieve the module object from sys.modules
    nnn = sys.modules["lib_addition_3ch_hor"]

    # Call the function from the imported module
    image1, image2, answer = nnn.get_image(1)
