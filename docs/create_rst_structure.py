from pathlib import Path
from shutil import copyfile


SOURCE_ROOT_FOLDER = "./source/"
Path(SOURCE_ROOT_FOLDER).mkdir(exist_ok=True)

with Path(SOURCE_ROOT_FOLDER, "index.rst").open(mode="w") as index_rst_file:
    index_rst_file.write("================================\n")
    index_rst_file.write("This is a documentation test\n")
    index_rst_file.write("================================\n")
    index_rst_file.write("\n\n")
    index_rst_file.write(".. toctree::\n")
    index_rst_file.write("   :maxdepth: 2\n")
    index_rst_file.write("\n")
    index_rst_file.write("   installation\n")
    index_rst_file.write("INSTALLATION\n")
    index_rst_file.write("==============\n")
    index_rst_file.write("\n")
    index_rst_file.write("To install this package, simply run the following command:\n")
    index_rst_file.write("\n")
    index_rst_file.write(".. code-block:: bash\n")
    index_rst_file.write("\n")
    index_rst_file.write("   pip install this_project\n")
    index_rst_file.write("\n")
    index_rst_file.write("This will install the package and all its dependencies.\n")
    index_rst_file.write("\n")
    index_rst_file.write("If you want to install the package in development mode, run the following command:\n")
    index_rst_file.write("\n")
    index_rst_file.write(".. code-block:: bash\n")
    index_rst_file.write("\n")
    index_rst_file.write("   pip install -e .\n")
    index_rst_file.write("\n")

copyfile("conf.py", Path("source", "conf.py"))
