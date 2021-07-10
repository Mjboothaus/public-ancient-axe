package := "old-ancient-axe"

# initial install of dependencies (from pyproject.toml)
pinstall:
  poetry install

# update of dependencies (from pyproject.toml)
pupdate:
  poetry update

# launch streamlit app
app:
  poetry run streamlit run streamlit_app.py &

# black and isort
lint:  
   black .

# build documentation 
docs:
  poetry run sphinx-build -a docs docs/site

# show documentation in browser
show:
  open docs/site/index.html

# publish documentation to Github Pages
pages:
  poetry run ghp-import docs/site 

# create rst source for API documentation
apidoc:
  sphinx-apidoc -o docs src/{{package}}

# list running Streamlit processes
ps:
  ps -ef | grep "streamlit run" | grep -v sh