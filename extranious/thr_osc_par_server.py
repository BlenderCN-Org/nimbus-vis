#enables standalone support
if __name__ == "__main__":
    import os
    import bpy
    import sys
    from os.path import dirname, join
    mainPackage = dirname(bpy.data.filepath)
    if not mainPackage in sys.path:
        sys.path.append(mainPackage)
        print(mainPackage + " appended to sys path")
    library = join(mainPackage, "libs")
    if not library in sys.path:
        sys.path.append(library)
        print(library + " appended to sys path")
    os.chdir(mainPackage) ###THIS IS VERY IMPORTANT AND FIXES EVERYTHING
        
    #extra file-specific stuff
    extr = join(mainPackage, "extranious")
    if not extr in sys.path:
        sys.path.append(extr)
        print(extr + " appended  to sys path")
    os.chdir(extr)
    
#######################################
import threading
