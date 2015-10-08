pytemperaturectrl - Python package
======================

This is a python library to communicate with temperature control unit. Work with Julabo Corio CD
[www.julabo.com](http://www.julabo.com)

### Some Samples

**open port, get version**
```python
>>> from pytemperaturectrl import julabo
>>> j = julabo.Julabo()
>>> j.open('COM4')
>>> j.getVersion()
'JULABO CORIO CD - 200F 230V 50Hz Version 2.4.1'
```

**close port**
```python
>>> j.close()
```
