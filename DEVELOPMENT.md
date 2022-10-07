# Development of this package


```
pip install hatch
hatch run pytest -sv
hatch build
```

## Release

```
pip install twine
hatch build
twine upload dist/*
```
