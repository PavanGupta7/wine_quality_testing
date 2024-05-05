step-0) template creation
step-1) git init
step-2) dvc init
step-3) dvc add data_give/winequality.csv
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/PavanGupta7/wine_quality_testing.git
git push -u origin main



#get data from the source #get_data.py
# load data and save it in data/raw/ #load_data.py
#created stages in DVC.yaml and "dvc repro"

#splitted the dataset into train and test
#created stages in DVC.yaml and dvc repro


#model training and model evaluation
#save the model using joblib

#creating "reports" folder where we will keep metrics and save it in params.json , and for score will be saved in scores.json
#now adding stages in dvc.yaml file


# Testing
# -Bash
#tox command
for rebuilding 
''' bash
tox -r

pytest commands
''' bash
pytest -v

setup commands -
'''bash
pip install -e .

#build your own packages commands
'''bash
python setup.py sdist bdist_wheel
