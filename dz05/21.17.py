import re

# регулярки
PATT_ADDR = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
PATT_HTTP = r"(?P<url>https?://[^\s]+)"
PATT_DATETIME = r"\b\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}\b"

# заборонені домени
FORBIDEN_SITES = ['vk.com', 'mail.ru', 'ok.ru', 'yandex.ru']

# відповідність IP → ім’я співробітника
WORKERS = {
    '123.123.123.123': 'Person1',
    '323.123.123.323': 'Person2',
    '987.654.153.123': 'Person3',
    '324.120.123.123': 'Person4'
}

def read_data_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return f.readlines()

def search_bad_workers(data):
    # рахуємо порушення
    count_visit = {ip: 0 for ip in WORKERS}

    for line in data:
        # шукаємо URL
        url_match = re.search(PATT_HTTP, line)
        if not url_match:
            continue

        full_url = url_match.group("url")
        domain = full_url.split("://")[1].split("/")[0]  # наприклад vk.com

        # перевірка, чи сайт заборонений
        if domain not in FORBIDEN_SITES:
            continue

        # шукаємо IP
        ip_match = re.search(PATT_ADDR, line)
        if not ip_match:
            continue

        ip = ip_match.group()

        # перевіряємо, чи IP належить працівнику
        if ip in WORKERS:
            count_visit[ip] += 1

    # формуємо статистику: (IP, (кількість, Ім’я))
    full_stats = {
        ip: (count_visit[ip], WORKERS[ip]) for ip in WORKERS
    }

    # сортуємо всіх
    all_sorted = sorted(full_stats.items(), key=lambda x: x[1][0], reverse=True)

    # тільки порушники >0
    violators = [item for item in all_sorted if item[1][0] > 0]

    return all_sorted, violators


if __name__ == "__main__":
    # читаємо файл логів
    text = read_data_file("21.17.txt")

    all_stat, bad_stat = search_bad_workers(text)

    print("Співробітники, які відвідували заборонені сайти:\n")
    for ip, (count, name) in bad_stat:
        print(f"{name} (IP: {ip}) — {count} раз(и)")
