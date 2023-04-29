# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['E:/tkinter_ml_app/ml_app.py'],
             pathex=['E:\\tkinter_ml_app'],
             binaries=[],
             datas=[('E:/tkinter_ml_app/trained_model/model.pkl', '.')],
             hiddenimports=['sklearn', 'sklearn.ensemble._forest', 'sklearn.neighbors._typedefs', 'sklearn.utils._weight_vector', 'sklearn.neighbors._quad_tree'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ml_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='E:\\tkinter_ml_app\\python_104451.ico')
