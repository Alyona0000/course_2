import re

def rozbyty_ta_zberehty(shlyah_do_vkhid: str, shlyah_do_vykhid: str) -> None:
    with open(shlyah_do_vkhid, 'r', encoding='utf-8') as f:
        tekst = f.read()

    pattern = r'(?<=[.!?])\s+'
    rechennya = re.split(pattern, tekst)
    rechennya = [r.strip() for r in rechennya if r.strip()]

    with open(shlyah_do_vykhid, 'w', encoding='utf-8') as f:
        for r in rechennya:
            f.write(r + '\n')


if __name__ == '__main__':
    rozbyty_ta_zberehty('vkhid.txt', 'rechennya.txt')
    print("Готово: речення збережені у файлі rechennya.txt")
