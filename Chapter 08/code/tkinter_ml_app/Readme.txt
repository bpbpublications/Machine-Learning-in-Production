For Venv in VS code----->
conda create -n venv_tkinter python=3.7 -y
source activate venv_tkinter
conda env remove -n venv_tkinter
=============================================================

Single file with icon but without console----------

pyinstaller --noconfirm --onefile --windowed --icon "E:/tkinter_ml_app/python_104451.ico" --add-data "E:/tkinter_ml_app/trained_model
/model.pkl;." --hidden-import "sklearn" --hidden-import "sklearn.ensemble._forest" --hidden-import "sklearn.neighbors._typedefs" --hidd
en-import "sklearn.utils._weight_vector" --hidden-import "sklearn.neighbors._quad_tree"  "E:/tkinter_ml_app/ml_app.py"

=============================================================
Single directory with console---------

pyinstaller --noconfirm --onedir --console --add-data "E:/tkinter_ml_app/trained_model
/model.pkl;." --hidden-import "sklearn" --hidden-import "sklearn.ensemble._forest" --hidden-import "sklearn.neighbors._typedefs" --hidd
en-import "sklearn.utils._weight_vector" --hidden-import "sklearn.neighbors._quad_tree"  "E:/tkinter_ml_app/ml_app.py"

=============================================================
Single file with console---------

pyinstaller --noconfirm --onefile --windowed --add-data "E:/tkinter_ml_app/trained_model
/model.pkl;." --hidden-import "sklearn" --hidden-import "sklearn.ensemble._forest" --hidden-import "sklearn.neighbors._typedefs" --hidd
en-import "sklearn.utils._weight_vector" --hidden-import "sklearn.neighbors._quad_tree"  "E:/tkinter_ml_app/ml_app.py"
==============================================================
Hidden imports-------------

sklearn
sklearn.ensemble._forest
sklearn.neighbors._typedefs
sklearn.utils._weight_vector
sklearn.neighbors._quad_tree