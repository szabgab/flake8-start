from flake8.api import legacy as flake8
import os
import sys
import re
from io import StringIO

# Given a directory path, run flake8 in that directory and return the data


def process(path_to_dir):
    python_files = get_python_files(path_to_dir)
    # TODO read .flake8 configuration file and generate the report accoringly
    report = run_flake8(python_files)
    full_text = {}
    reports = {}
    #for key in ['A', 'E', 'F', 'W']:
    for code in range(ord('A'), ord('Z')+1):
        key = chr(code)
        rep = report.get_statistics(key)
        for entry in rep:
            #print(entry)
            # 2 F401 '.controllers' imported but unused
            match = re.search(r'^\d+\s(\w+)\s', entry)
            if not match:
                print(f"ERROR: Line '{entry}' not matched. Please report to the developers of flake8-start")
                continue
            code = match.group(1)
            if code not in reports:
                full_text[code] = entry
                reports[code] = 0
            reports[code] += 1
    return full_text, reports


# The check_files call prints the report to STDOUT as well.
# So in this function we capture that and discard that output.
def run_flake8(python_files):
    if not python_files:
        return {}
    style_guide = flake8.get_style_guide()
    backup = sys.stdout
    sys.stdout = StringIO()
    report = style_guide.check_files(python_files)
    #    out = sys.stdout.getvalue()
    sys.stdout = backup
    return report


def get_python_files(path_to_dir):
    if os.path.isfile(path_to_dir):
        return [path_to_dir]
    python_files = []
    for dirname, dirs, files in os.walk(path_to_dir):
        for filename in files:
            if not filename.endswith('.py'):
                continue

            path = os.path.join(dirname, filename)   # relative path to the "current" file
            python_files.append(path)
    return python_files

# '/home/gabor/x/e-commerce'
if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} PATH")
    source_path = sys.argv[1]
    flake8_file = os.path.join(source_path, '.flake8')
    if os.path.exists(flake8_file):
        exit(f"The file {flake8_file} already exists. Please remove it or rename it and then run this code again.")

    full_text, reports = process(source_path)

    if not full_text:
        print("The code is clean from any flake8 issues")
        exit()

    with open(flake8_file, 'w') as fh:
        for code in sorted(full_text.keys()):
            fh.write(f"# {code} - ({reports[code]}) - {full_text[code]}\n")
        fh.write("\n\n")
        fh.write("[flake8]\n")
        fh.write("ignore =\n")
        fh.write("    *.py " + " ".join(sorted(full_text.keys())) + "\n")

