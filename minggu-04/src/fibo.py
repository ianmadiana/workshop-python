# Modules
# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
# fibo.fib(199)
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144 
# fibo.fib2(200)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# fibo.__name__
# output: 'fibo'
# fib(200)
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144

# More on Modules
from fibo import fib, fib2
# fib(200)
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144
from fibo import *
# fib(200)
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144
import fibo as fib
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
from fibo import fib as fibonacci
# output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

# Executing modules as scripts
# terminal: python fibo.py 100
# output: 0 1 1 2 3 5 8 13 21 34 55 89

# The dir() Function
dir(fibo)
# ['__builtins__','__cached__','__doc__','__file__','__loader__','__name__','__package__','__spec__','fib','fib2']
dir(sys)
# output:
# ['__breakpointhook__','__displayhook__','__doc__','__excepthook__','__interactivehook__','__loader__','__name__','__package__','__spec__','__stderr__','__stdin__','__stdout__','__unraisablehook__','_base_executable','_clear_type_cache','_current_exceptions','_current_frames','_deactivate_opcache','_debugmallocstats','_enablelegacywindowsfsencoding','_framework','_getframe','_git','_home','_xoptions','addaudithook','api_version','argv','audit','base_exec_prefix','base_prefix','breakpointhook','builtin_module_names','byteorder','call_tracing','copyright','displayhook','dllhandle','dont_write_bytecode','exc_info','excepthook','exec_prefix','executable','exit','flags','float_info','float_repr_style','get_asyncgen_hooks','get_coroutine_origin_tracking_depth','get_int_max_str_digits','getallocatedblocks','getdefaultencoding','getfilesystemencodeerrors','getfilesystemencoding','getprofile','getrecursionlimit','getrefcount','getsizeof','getswitchinterval','gettrace','getwindowsversion','hash_info','hexversion','implementation','int_info','intern','is_finalizing','last_traceback','last_type','last_value','maxsize','maxunicode','meta_path','modules','orig_argv','path','path_hooks','path_importer_cache','platform','platlibdir','prefix','ps1','ps2','ps3','pycache_prefix','set_asyncgen_hooks','set_coroutine_origin_tracking_depth','set_int_max_str_digits','setprofile','setrecursionlimit','setswitchinterval','settrace','stderr','stdin','stdlib_module_names','stdout','thread_info','unraisablehook','version','version_info','warnoptions','winver']

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
# output:
# ['In','Out','_','_25','_26','_31','_32','_6','_7','_8','__','___','__builtin__','__builtins__','__doc__','__loader__','__name__','__package__','__spec__','_dh','_i','_i1','_i10','_i11','_i12','_i13','_i14','_i15','_i16','_i17','_i18','_i19','_i2','_i20','_i21','_i22','_i23','_i24','_i25','_i26','_i27','_i28','_i29','_i3','_i30','_i31','_i32','_i33','_i34','_i35','_i36','_i4','_i5','_i6','_i7','_i8','_i9','_ih','_ii','_iii','_oh','a','exit','fib','fib2','fibo','fibonacci','get_ipython','open','quit','sys']

import builtins
dir(builtins)
# output:
# ['ArithmeticError','AssertionError','AttributeError','BaseException','BlockingIOError','BrokenPipeError','BufferError','BytesWarning','ChildProcessError','ConnectionAbortedError','ConnectionError','ConnectionRefusedError','ConnectionResetError','DeprecationWarning','EOFError','Ellipsis','EncodingWarning','EnvironmentError','Exception','False','FileExistsError','FileNotFoundError','FloatingPointError','FutureWarning','GeneratorExit','IOError','ImportError','ImportWarning','IndentationError','IndexError','InterruptedError','IsADirectoryError','KeyError','KeyboardInterrupt','LookupError','MemoryError','ModuleNotFoundError','NameError','None','NotADirectoryError','NotImplemented','NotImplementedError','OSError','OverflowError','PendingDeprecationWarning','PermissionError','ProcessLookupError','RecursionError','ReferenceError','ResourceWarning','RuntimeError','RuntimeWarning','StopAsyncIteration','StopIteration','SyntaxError','SyntaxWarning','SystemError','SystemExit','TabError','TimeoutError','True','TypeError','UnboundLocalError','UnicodeDecodeError','UnicodeEncodeError','UnicodeError','UnicodeTranslateError','UnicodeWarning','UserWarning','ValueError','Warning','WindowsError','ZeroDivisionError','__IPYTHON__','__build_class__','__debug__','__doc__','__import__','__loader__','__name__','__package__','__spec__','abs','aiter','all','anext','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','copyright','credits','delattr','dict','dir','display','divmod','enumerate','eval','exec','execfile','filter','float','format','frozenset','get_ipython','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','license','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','runfile','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']​
