# Linux
sudo apt-get install python3-venv    # If needed  
python3 -m venv .venv  
source .venv/bin/activate  

# macOS
python3 -m venv .venv  
source .venv/bin/activate  

# Windows
py -3 -m venv .venv  
.venv\scripts\activate

# Install requirements  
pip install -r requirements.txt  
  
# Run tests  
coverage run -m unittest tests.py  

# Run tests coverage report  
coverage report -m  