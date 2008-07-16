'''
Figure out some interesting information about the source code.

This is based closely on test_status.py

to ignore directories, put them as aruments to the script, so for instance:
$ python stats.py dev/
will ignore all files contained in dev/

I suggest running this script with the following arguments to ignore irrelevant directories:
$ python stats.py dev/ server_root/ src/tests/ src/element_tree/

The following statistics are gathered:
 * Total number of .py files
 * Total number of Classes
 * Total number of Functions/Methods
 * Number of functions/methods marked as tested
 * List of .py files ordered by percentage tested
 * A dependency graph rendered using dot,

maybe one day we can some kind of automated coverage analsis (maybe that should be in all_tests.py)
'''
import sys
import os
import os.path
import re
from subprocess import Popen, PIPE

import_re = re.compile(r"\s*(import|from)\s+(?P<module>[_a-zA-Z][_0-9a-zA-Z\.]*)")
def_re = re.compile(r"\s*?def\s+(?P<fname>[_a-zA-Z][_0-9a-zA-Z]*)")
class_re = re.compile(r"\s*?class\s+(?P<cname>[_a-zA-Z][_0-9a-zA-Z]*)")

tested_re = re.compile(r"#\s*tested\s*$")
empty_re = re.compile(r"\s*$")

def main(ignore_these):
    """The main function, called when this file is run as a script"""
    os.chdir(os.path.pardir)
    # get a list of all files and directories in the distribution
    file_list = []
    os.path.walk('.', (lambda _, dirname, fnames : file_list.extend([os.path.join(dirname, f)[2:] for f in fnames])), {})

    # filter the list to remove things in ignore_these
    for ignore in ignore_these:
        file_list = [f for f in file_list if not f.startswith(ignore)]
    
    # filter that list to get the python files
    py_file_list = [f for f in file_list if f.endswith('.py')]

    # examine the py files
    total_lines = 0
    total_functions = 0
    total_classes = 0
    total_tested = 0
    py_file_info = {}
    for f in py_file_list:
        lines, imports, functions, classes, tested = examine_file(f)
        py_file_info[f] = lines, imports, functions, classes, tested
        total_lines += lines
        total_functions += functions
        total_classes += classes
        total_tested += tested

    print
    print "%d python source files, containing %d lines." % (len(py_file_list), total_lines)
    print "In all there are %d functions and %d classes, %d%%(%d) of which are tested." % (total_functions, total_classes, total_tested*100 / (total_functions + total_classes), total_tested)
    print
    print '*' * 80
    print 'Tested\tFile'

    def cmp(a, b):
        if py_file_info[a][4] == 0:
            return 1
        if py_file_info[b][4] == 0:
            return -1
        if (py_file_info[a][4] *100.0/(py_file_info[a][3] + py_file_info[a][2])) < (py_file_info[b][4] *100.0/(py_file_info[b][3] + py_file_info[b][2])):
            return 1
        else:
            return -1

    py_file_list.sort(cmp)

    for f in py_file_list:
        if py_file_info[f][4] > 0:
            print '%3d%%\t%s' % (py_file_info[f][4] *100.0/(py_file_info[f][3] + py_file_info[f][2]), f)
        elif py_file_info[f][3] + py_file_info[f][2] == 0:
            # no classes or functions or tests - this is OK
            print ' N/A\t%s' % f
        else:   # functions, but no tests :(
            print '  0%%\t%s' % f

    build_graph(py_file_info)

def examine_file(f):
    """examine the file f and return lots of information about it"""
    stream = open(f, 'rt')
    lines = 0
    imports = []
    functions = 0
    classes = 0
    tested = 0

    for line in stream:
        # is this an empty line?
        if re.match(empty_re, line):
            continue

        # note that empty lines aren't counted
        lines += 1

        # is the line an import statement?
        result = re.match(import_re, line)
        if result:
            imports.append(result.groupdict()['module'])
            continue

        result = re.match(def_re, line)
        if result:
            functions += 1
            # this is a candidate for testing:
            if re.search(tested_re, line):
                tested += 1

        result = re.match(class_re, line)
        if result:
            classes += 1
            # this is a candidate for testing:
            if re.search(tested_re, line):
                tested += 1

    stream.close()
    return lines, imports, functions, classes, tested

def build_graph(py_file_info):
    """Build a graph using dot"""
    process = Popen("dot -Tps2 -o dependencies.ps", shell=True, stdin=PIPE)
    dot_descr = 'digraph dependencies { graph [page="8,11" pagedir=TR]'
    # generate the vertices
    # keeping track of vertices generated
    vertices = []
    for fname in py_file_info:
        mname = fname.split('/')[-1].split('.')[0]
        if mname == "__init__":
            # here we us the folder name as the module name
            try:
                mname = fname.split('/')[-2].split('.')[0]
            except IndexError:
                continue
        dot_descr += '%s [label="%s"]\n' % (mname, fname)
        vertices.append(mname)
    # generate the edges
    for fname in py_file_info:
        mname = fname.split('/')[-1].split('.')[0]
        for dmname in py_file_info[fname][1]:
            dmname = dmname.split('.')[-1]
            if dmname not in vertices:
                # ignore modules that are outside the crunchy distro:
                continue
            dot_descr += "%s -> %s\n" % (mname, dmname)
    dot_descr += '}'
    process.communicate(dot_descr)

if __name__ == "__main__":
    ignore_these = sys.argv[1:]
    main(ignore_these)
