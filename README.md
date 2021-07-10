# old-ancient-axe -- "No data in Excel" :)

Prototype (Streamlit) App to deconstruct / summarise etc Excel workbooks. Add button to upload Excel file (no-PII data please!) and then parse it for data - possibly push to SQLite / summary (data quality?) / charts(?) / insights.

Building this Streamlit App as just a .py script (not Notebooks via `nbdev`) to compare workflows.

Minimal setup to work with Poetry, Sphinx and Streamlit out of the box.

## CookieCutter Template Features

See here for details: 
* https://github.com/cjolowicz/cookiecutter-hypermodern-python

 - [streamlit](https://docs.streamlit.io/en/stable/) for quick dashboards
 - [Poetry](https://python-poetry.org/) package and environment manager
 - [pytest](https://docs.pytest.org/en/stable/) and [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) testing pipeline
 - [Sphinx](https://www.sphinx-doc.org/en/master/) documentation with:
   - markdown support via powerful [myst-parser](https://myst-parser.readthedocs.io/en/latest/)
   - beautiful [PyData theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/)
   - publishing documentation to Github Pages
- justfile for [just](https://github.com/casey/just) command runner
- MIT license
