from rich import print
from time import sleep

def print_lyrics_vivo():
    lines = [
        ("E-ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),
        ("Vai quicando, vai jogando, não perde a razão", 0.045),
        ("No batidão, no batidão, só pura tentação", 0.045),

        ("Ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),
        ("Ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),

        ("Ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),
        ("Vai quicando, vai jogando, não perde a razão", 0.045),
        ("No batidão, no batidão, só pura tentação", 0.045),

        ("Ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),
        ("Ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),

        ("Ela desce, ela sobe, no baile é pressão", 0.04),
        ("Mina linda, perigosa, rouba meu coração", 0.04),
    ]

    for text, delay in lines:
        for char in text:
            print(f"[bold cyan]{char}[/bold cyan]", end="", flush=True)
            sleep(delay)
        print()
        sleep(0.25)

    for text, delay in lines:
        for char in text:
            print(f"[bold magenta]{char}[/bold magenta]", end="", flush=True)
            sleep(delay)
        print()
        sleep(0.25)

if __name__ == "__main__":
    print("[bold magenta]🎶 Starting the lyrics...[/bold magenta]\n")
    print_lyrics_vivo()
    print("\n[bold green]✅ Done! Play the song and enjoy 🔥[/bold green]")