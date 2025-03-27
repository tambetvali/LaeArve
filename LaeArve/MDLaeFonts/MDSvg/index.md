# Laegna Svg Font

## Displaying basic Laegna Numbers

The font displays the characters with such spacing:
- If there are no accents on left or right, the letter spacing is normal.
- If accents left or right are on the same side of each character, they are *close* and then the font is less wide.
- If they are on both sides, the font is wide - there is enough space between letters to contain the accents.

Class LaeSvgLetter:
  def __init__(self, letter = , accents = [None] * 8)

Class LaeSvg:
  def __init__