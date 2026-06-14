from jmcomic_downloader.text import show_welcome_banner
from rich.console import Console
fonts_ls = """Standard
Slant
3-D
5lineoblique
Alphabet
Banner3-D
Doh
Isometric1
Letters
Alligator
Digital
Bubble
Bulbhead""".split("\n")

console = Console()
for font in fonts_ls:
    console.print(f"\n\n\n----------{font}----------")
    console.print(show_welcome_banner(font))
    