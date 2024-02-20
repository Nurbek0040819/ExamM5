import requests

def save_page_as_pdf(url, pdf_filename):
    response = requests.get(url)
    with open(pdf_filename, 'wb') as pdf_file:
        pdf_file.write(response.content)


base_url = 'https://tilshunos.com/omonims/?page='
for page_num in range(1, 21):
    url = base_url + str(page_num)
    pdf_filename = f'page_{page_num}.pdf'
    save_page_as_pdf(url, pdf_filename)
    print(f'{url} sahifasi PDF formatiga olingan.')

print('Barcha sahifalar PDF formatiga olingan.')
