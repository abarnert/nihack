import ast
import importlib
import importlib.machinery
import sys

class NiTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        node.s = 'Ni! Ni! Ni!'
        return node

class NiLoader(importlib.machinery.SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):
        source = importlib._bootstrap.decode_source(data)
        tree = NiTransformer().visit(ast.parse(source, path, 'exec'))
        return compile(tree, path, 'exec')

finder = sys.meta_path[-1]
loader = finder.find_module(__file__)
loader.source_to_code = NiLoader.source_to_code
