from cx_Freeze import setup, Executable

setup(name="Transporticular",
      version="8",
      description="Transport tycoon game",
      executables=[Executable(script="transport_8.py",
                              base="Win32GUI",
                              icon="data/icon.ico")])
