 
import os

# Create the main project directory
project_dir = "recommendation_engine"
os.mkdir(project_dir)
os.chdir(project_dir)

# Create subdirectories
data_dir = "data"
src_dir = "src"
api_dir = "api"
ui_dir = "ui"
for directory in [data_dir, src_dir, api_dir, ui_dir]:
    os.mkdir(directory)

# Create empty files in each directory
data_files = ["user_data.csv", "item_data.csv"]
src_files = ["__init__.py", "data_loader.py", "data_transformer.py", "recommender.py"]
api_files = ["__init__.py", "main.py"]
ui_files = ["__init__.py", "main.py"]

for file in data_files:
    open(os.path.join(data_dir, file), "w").close()

for file in src_files:
    open(os.path.join(src_dir, file), "w").close()

for file in api_files:
    open(os.path.join(api_dir, file), "w").close()

for file in ui_files:
    open(os.path.join(ui_dir, file), "w").close()
