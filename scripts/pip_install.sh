# Please execute the following command in a unix console/terminal 

# creating a path for module installation 
mkdir -p /Users/student/tmp/Python/2.7/site-packages/

# adding the above path to the pythonpath env variable 
export PYTHONPATH=$PYTHONPATH:/Users/student/tmp/Python/2.7/site-packages/

# install the machine learning package
pip install freeze scikit-learn  
#pip install --install-option="--prefix=$PREFIX_PATH" package_name 

# testing the installation
python -c "import sklearn"

# uninstalling the module 
pip uninstall scikit-learn
