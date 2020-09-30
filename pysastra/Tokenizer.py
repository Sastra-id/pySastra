from abc import ABC, abstractmethod
from .utils import overridden, string_span_tokenize, regexp_span_tokenize

class TokenizerI(ABC): 
    @abstractmethod
    def tokenize(self, s): 
        if overridden(self.tokenize_sents):
            return self.tokenize_sents([s])[0]

    def span_tokenize(self, s): 
        raise NotImplementedError()

    def tokenize_sents(self, strings): 
        return [self.tokenize(s) for s in strings]

    def span_tokenize_sents(self, strings): 
        for s in strings:
            yield list(self.span_tokenize(s))

class StringTokenizer(TokenizerI): 
    
    @property
    @abstractmethod
    def _string(self):
        raise NotImplementedError

    def tokenize(self, s):
        return s.split(self._string)

    def span_tokenize(self, s):
        for span in string_span_tokenize(s, self._string):
            yield span

class Tokenizer(StringTokenizer):
    _string = " "

class LineTokenizer(TokenizerI):

    def __init__(self, blanklines="discard"):
        valid_blanklines = ("discard", "keep", "discard-eof")
        if blanklines not in valid_blanklines:
            raise ValueError(
                "Blank lines must be one of: %s" % " ".join(valid_blanklines)
            )
        self._blanklines = blanklines
        
    def tokenize(self, s):
        lines = s.splitlines()
        
        if self._blanklines == "discard":
            lines = [l for l in lines if l.rstrip()]
        elif self._blanklines == "discard-eof":
            if lines and not lines[-1].strip():
                lines.pop()
        return lines
    
    def span_tokenize(self, s):
        if self._blanklines == "keep":
            for span in string_span_tokenize(s, r"\n"):
                yield span
        else:
            for span in regexp_span_tokenize(s, r"\n(\s+\n)*"):
                yield span

