from distutils.core import setup
import py2exe

#setup( options = {'py2exe': {'bundle_files':1, 'compressed': True }},
#       windows = ['D3WeaponReroll.pyw'],
#       zipfile = None,
#      )

setup(
    windows = [
        {
            "script":"D3WeaponReroll.pyw",
            "icon_resources": [ (1, "D3Caculator.ico") ]
        }
    ],
)
