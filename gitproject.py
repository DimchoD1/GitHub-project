import requests
import json

token = 'ГИТ_ТОКЕН'
repository = 'РЕПОЗИТОРИЙ'

def create_issue(title, body):
    url = f'https://api.github.com/repos/{repository}/issues'
    headers = {'Authorization': f'token {token}'}
    data = {'title': title, 'body': body}
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print(f'Проблемът "{title}" беше успешно създаден.')
    else:
        print(f'Грешка при създаването на проблем: {response.status_code}, {response.text}')


create_issue('Проблем 1', 'Това е проблем номер едно.')
