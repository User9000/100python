
import glob

print(len(glob.glob('subdirs/**/*.py',recursive=True)))

