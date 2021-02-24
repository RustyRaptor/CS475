# clone the repo
git clone https://github.com/aimacode/aima-python.git

cd aima-python

# install dependencies
python3 -m pip install -r requirements.txt

# downlaod the test data 
git submodule init
git submodule update

# install pytest
python3 -m pip install pytest

# test the code
py.test
