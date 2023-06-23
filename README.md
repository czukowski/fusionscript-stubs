DaVinci Resolve Python API stubs
================================

Installation
------------

```sh
$ pip install fusionscript-stubs
```

Alternatively, drop `fusionscript.pyi` somewhere your IDE will find it and adjust
your import statements accordingly.

How to use
----------

Add this on top of your script:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fusionscript import Resolve  # ...and/or other types you want
```

You may then use these imported types in your code and get type hints, but they have 
to be quoted, for example:

```python
def GetResolve() -> 'Resolve':
    ...
```

Happy scripting!

Patches are welcome to fix any errors in the stubs!

About versioning
----------------

The stubs package major and minor version numbers (eg. 18.1) indicate compatibility 
with the corresponding DaVinci Resolve version and is based on the documentaton 
(scripting README.txt) shipped with that version. The patch version number is incremental
and does not correspond to DaVinci Resolve releases.

The current stubs are based on the documentation marked as "Updated as of 22 Nov 2022". 
