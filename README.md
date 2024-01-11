

Uses [Hatch](https://pypi.org/project/hatch/) as a build backend by default.

To install build tools:
```
py -m pip install --upgrade build
```

To build:
```
py -m build
```

To upload the package, install Twine: 
```
py -m pip install --upgrade twine
```

To upload the package:
```
py -m twine upload --repository testpypi dist/*
```
  username = __token__
  password = pypi-[THE TOKEN YOU GOT FROM test.pypi.org/]
```

To install the package from the test repository:
```
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps PyEasyMidiFileParserCpp
```

To use the package in your code:
```py
from PyEasyMidiFileParserCpp import *
```

To install locally:
```
pip install -e ./
```

# https://youtu.be/QMY-OkckDwo

export PYTHONPATH=$PYTHONPATH:C:\Users\thoma\PandorasBox\Projects\ModularMusicGenerationModules\Modules\RuntimeModules\PyEasyMidiFileParserCpp