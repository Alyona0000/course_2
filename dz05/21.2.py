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

    print("Готово! Речення записано у файл:", shlyah_do_vykhid)


rozbyty_ta_zberehty(
    r"C:\Users\alenk\Repository\Course_2\dz05\vkhid.txt",
    r"C:\Users\alenk\Repository\Course_2\dz05\rechennya.txt"
)
