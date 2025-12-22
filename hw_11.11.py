from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Book:
    title: str
    authors: List[str] = field(default_factory=list)
    year: int | None = None

    def formatted(self):
        if self.year and self.authors:
            return f'{self.title} ({self.year}) - {", ".join(self.authors)}'
        elif self.year:
            return f'{self.title} ({self.year})'
        elif self.authors:
            return f'{self.title} - {", ".join(self.authors)}'
        else:
            return f'{self.title}'


b1 = Book('Python 101', ['John Doe'], 1883)
b2 = Book('Безымянная книга')
b3 = Book('Совместный труд', ['Alice', 'Bob'])
for b in (b1, b2, b3):
    print(b.formatted())