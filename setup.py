from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "sys", "winsound", "wx", "time", "sounds"],
    "include_files": [("sounds", "sounds")]
}

setup(
    name = "poetry master",
    version = "1.0",
    description = "A Poetry quiz game using riddles",
    options = {"build_exe": build_exe_options},
    executables = [Executable("poetry_master_game.py", base = "Win32GUI")]
)