'''Sort and remove duplicates'''
from json import dumps

PLAINTEXT_FILENAME = 'list.txt'
JSON_FILENAME = 'urls.json'

with open(PLAINTEXT_FILENAME, encoding='utf-8') as plaintext_file:
    domains = sorted(set(domain.strip() for domain in plaintext_file.readlines()))

with open(PLAINTEXT_FILENAME, 'w', encoding='utf-8') as plaintext_file:
    plaintext_file.writelines(f'{domain}\n' for domain in domains)

with open(JSON_FILENAME, 'w', encoding='utf-8') as json_file:
    json_file.write(f'{dumps(domains, ensure_ascii=False, indent=2)}\n')
