# -*- mode: python -*-
a = Analysis(['D3WeaponReroll.pyw'],
             pathex=['/home/rocky/Dropbox/WorkSpace/Python/D3WeaponReroll'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='D3WeaponReroll',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='D3Caculator.ico')
