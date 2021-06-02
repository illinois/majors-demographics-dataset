# Fetch data
wget https://www.dmi.illinois.edu/stuenr/ -r 0

# Install deps and wrangle
pip install xlrd
python reproduce.py
