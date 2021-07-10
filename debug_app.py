# https://stackoverflow.com/questions/60172282/how-to-run-debug-a-streamlit-application-from-an-ide

# Debugging Streamlit app work-a-round

from streamlit import bootstrap

app_script = 'streamlit_app.py'

bootstrap.run(app_script, f'debug_app.py {app_script}', [], {})