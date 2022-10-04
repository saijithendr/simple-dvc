create env

```wind cmd
conda create -n wineq python=3.9 -y
```

activate env
```window cmd
activate wineq
```

created requirements file

install the reqmnts
``` window cmd
pip install -r requirements.txt
````

Download the data from "https://www.kaggle.com/datasets/sh6147782/winequalityred" to data_given directory

```
git init
```
```
dvc init
```
```
dvc add data_given/winequality.csv
```

```
git add .
```
```
git commit -m "first commit"
```
```
git add . && git commit -m "update Readme.md"
```

```
git remote add origin https://github.com/c17hawke/simple-dvc-demo.git
git branch -M main
git push origin main
```
tox command -
```
tox
```
for rebuilding
```
tox -r
```
pytest command
```
pytest -v
```

ssetup commands -
```
pip install -e .
```

build your own package commands
```
python setup.py sdist bdist wheel
```
