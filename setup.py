# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="pramanpatram",
    version="1.0.0",
    description="Python Library for Generating Event Certificates",
    long_description="""A simple Python library for Structural Beam Analysis developed by students of Kakatiya Institute of Technology and Science for Civil Engineering Applications
                    Python Library for Beam Analysis for Civil Engineering

Developed by Aryan Karamtoth from Information Technology Department at Kakatiya Institute of Technology and Science

## Supported Features

- Making a beam
- Calculating Support Reactions of a beam
- Applying load on a beam

## Installation

```
pip install pramanpatram
```
## Getting Started

Import the package

```py
import pramanpatram as patra
```
Read the documentation and apply the required method for your purpose

## Documentation

### Built-in Methods:
- `createBeam(len)`:
Method for creating a beam

    Input:  len  --> Length of Beam
    Output: beam --> Beam object

Example:
```py
beam = bm.createBeam(10)
print(beam)
```

- `definePin(pinPos,beam)`:

Method for defining the position of pin support

    Input:  pinPos      --> Pin Support Position
            beam        --> Beam object
    Output: pinposition --> Pin Position

Example:
```py
pinpos = bm.definePin(2,beam)
print(pinpos)
```

- `defineRoller(rollPos,beam)`:

  Method for defining the position of roller support

    Input:  rollPos --> Roller Support Position
            beam    --> Beam object

    Output: rollposition --> Roller Position

  Example:
  ```py
  rollpos = bm.defineRoller(4,beam)
  print(rollpos)
  ```
- `applyPointLoad(loadPos,loadMag,beam)`:

  Method for applying Point Load on the beam

    Input:  loadPos --> Position of Point Load
            loadMag --> Magnitude of Point Load
            beam    --> Beam object

    Output: load    --> Applied Load 

  Example:
  ```py
  ptload = bm.applyPointLoad(4,60,beam)
  print(ptload)
  ```

- `applyUDL(beam,loadPerUnitLength)`:

  Method for applying UDL (Uniformly Distributed Load) on the beam

    Input:  beam              --> Beam object
            loadPerUnitLength --> Load Per Unit Length

    Output: udl               --> Applied UDL

  Example:

  ```py
  udlarray = bm.applyUDL(beam,20)
  print(udlarray)
  ```

- `applyUVL(beam,startLoad,endLoad)`:

  Method for applying UVL (Uniformly Varying Load) on the beam

    Input:  beam       --> Beam object
            startLoad  --> Start Load
            endLoad    --> End Load

    Output: uvl        --> Applied UVL

  Example:
  ```py
  uvlarray = bm.applyUVL(beam,20,40)
  print(uvlarray)
  ```
- `applyMoment(momentPos, momentMag, beam)`:

  Method for applying Moment on the beam

    Input:  momentPos --> Moment Position
            momentMag --> Moment Magnitude
            beam      --> Beam Object

    Output: moments    --> Moment Applied

  Example:
  ```py
  appliedmoment = bm.applyMoment(3,20,beam)
  print(appliedmoment)
  ```
- `calcReactionsSSB(loads, pinPos, rollPos, beam)`:

  Method for calculation support reaction of a simply supported beam with various loads

    Input:  loads    --> Dictionary containing load data
            beam     --> Beam Object
            pinPos   --> Pin Position
            rollPos  --> Roller Support Position

    Output: Ra       --> Reaction at pin support
            Rb       --> Reaction at roller support

  Example:

  ```py
    loads = [
    {'type': 'point', 'position': 2, 'magnitude': 50},
    {'type': 'udl', 'start': 3, 'end': 5, 'magnitude': 20},
    {'type': 'uvl', 'start': 6, 'end': 8, 'start_magnitude': 10, 'end_magnitude': 30}
    ]
    pinPos = 1
    rollPos = 9
    Ra, Rb = bm.calcReactionsSSB(loads, pinPos, rollPos, beam)
    print(Ra)
    print(Rb)
  ```



                     """

    ,
    long_description_content_type="text/markdown",
    url="https://github.com/SpaciousCoder78/pramanpatram-lib",
    author="Aryan Karamtoth",
    author_email="aryankmmiv@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent"
    ],
    packages=["pramanpatram"],
    include_package_data=True,
    install_requires=["pandas","PIL","textwrap", "setuptools"]
)