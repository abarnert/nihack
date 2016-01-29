import importlib
import importlib.machinery
import sys

def ni_transform(c):
    consts = []
    for const in c.co_consts:
        if isinstance(c, str):
            consts.append('Ni! Ni! Ni!')
        elif isinstance(c, types.CodeType):
            consts.append(ni_transform(const))
        else:
            consts.append(const)
    return types.CodeType(
        c.co_argcount, c.co_kwonlyargcount, c.co_nlocals, c.co_stacksize,
        c.co_flags, c.co_code, tuple(consts), c.co_names, c.co_varnames,
        c.co_filename, c.co_name, c.co_firstlineno, c.co_lnotab,
        c.co_freevars, c.co_cellvars)

class NiLoader(importlib.machinery.SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):
        return ni_transform(compile(data, path, 'exec'))

finder = sys.meta_path[-1]
loader = finder.find_module(__file__)
loader.source_to_code = NiLoader.source_to_code
