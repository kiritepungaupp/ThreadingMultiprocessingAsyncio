import threading
import time
import requests
from bs4 import BeautifulSoup

def fetch_and_save_html(web_url):
    response = requests.get(web_url)
    time.sleep(3)
    parsed_content = BeautifulSoup(response.text, 'html.parser')
    page_title = parsed_content.title.string.strip() if parsed_content.title else 'default_page'
    output_filename = f"{page_title}.html"
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(response.text)

def run_io_tasks():
    urls_to_process = [
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "https://en.wikipedia.org/wiki/Photovoltaics",
        "https://en.wikipedia.org/wiki/Time_management",
        "https://en.wikipedia.org/wiki/Healthy_diet",
        "https://en.wikipedia.org/wiki/History_of_video_games",
        "https://en.wikipedia.org/wiki/Space_exploration",
        "https://en.wikipedia.org/wiki/Color_theory",
        "https://en.wikipedia.org/wiki/Sustainable_energy",
        "https://en.wikipedia.org/wiki/Cognitive_dissonance",
    ]
    
    thread_list = []
    for web_url in urls_to_process:
        new_thread = threading.Thread(target=fetch_and_save_html, args=(web_url,))
        thread_list.append(new_thread)
        new_thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    execute_io_operations()
