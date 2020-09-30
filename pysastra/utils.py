from re import finditer
import types

def string_span_tokenize(s, sep): 
    if len(sep) == 0:
        raise ValueError("Token delimiter must not be empty")
    left = 0
    while True:
        try:
            right = s.index(sep, left)
            if right != 0:
                yield left, right
        except ValueError:
            if left != len(s):
                yield left, len(s)
            break

        left = right + len(sep)


def regexp_span_tokenize(s, regexp): 
    left = 0
    for m in finditer(regexp, s):
        right, next = m.span()
        if right != left:
            yield left, right
        left = next
    yield left, len(s)


def spans_to_relative(spans): 
    prev = 0
    for left, right in spans:
        yield left - prev, right - left
        prev = right



def overridden(method): 
    if isinstance(method, types.MethodType) and method.__self__.__class__ is not None:
        name = method.__name__
        funcs = [
            cls.__dict__[name] 
            for cls in _mro(method.__self__.__class__) 
            if name in cls.__dict__
        ]
        return len(funcs) > 1
    else:
        raise TypeError("Expected an instance method.")
    

def _mro(cls): 
    if isinstance(cls, type):
        return cls.__mro__
    else:
        mro = [cls]
        for base in cls.__bases__:
            mro.extend(_mro(base))
        return mro

