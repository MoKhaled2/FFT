# Complex Number FFT Implementation

This Python project implements the Fast Fourier Transform (FFT) algorithm using a custom `Complex` class to handle complex numbers. The program processes a signal (list of numbers) provided by the user, calculates its FFT, and outputs the result.

## Features

1. **Custom Complex Number Class:**
   - Supports addition, subtraction, and multiplication of complex numbers.
   - Overrides `__str__` for a readable complex number representation.
   - Handles both real and imaginary components seamlessly.

2. **FFT Algorithm:**
   - Efficient implementation of the Fast Fourier Transform.
   - Handles signals of arbitrary length, padding them with zeros to the next power of 2.
   - Utilizes recursive computation and the twiddle factor for frequency domain transformations.

3. **Interactive User Input:**
   - Allows users to input the size and values of the signal dynamically.
   - Displays results in a formatted and easy-to-read table.

## Code Overview

### `Complex` Class

The `Complex` class provides operations for complex numbers:

- **`__add__`:** Adds two complex numbers.
- **`__sub__`:** Subtracts one complex number from another.
- **`__mul__`:** Multiplies two complex numbers.
- **`__str__`:** Outputs a formatted string representation of a complex number.

### FFT Algorithm

1. **Twiddle Factor:**
   - Calculates the complex exponential factor used in FFT.

2. **Signal Preparation:**
   - Pads the signal to the nearest power of 2.

3. **FFT Computation:**
   - Recursively divides the signal into smaller sections.
   - Applies the FFT computation using the twiddle factor and combines the results.

### Input and Output

- Prompts the user to input the signal size (`N`) and signal values.
- Outputs the computed FFT results in a structured format.

## How to Run the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/MoKhaled2/fft-complex.git
   cd fft-complex
## Example

### Input:
```
How many N do you Want to enter: 4
enter 1 number: 1
enter 2 number: -1
enter 3 number: 0
enter 4 number: 1

```

### Output:
```
-------------
|  NO NAME  |
-------------

THE RESULT IS:
------------------------------
|  X[0] = 1.00 + 0.00i
|  X[1] = 1.00 - 2.00i
|  X[2] = 1.00 + 0.00i
|  X[3] = 1.00 + 2.00i
------------------------------

```

## License

This project is licensed under the [MIT License](LICENSE).
