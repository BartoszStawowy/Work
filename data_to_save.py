from datetime import datetime
import os


def data_to_txt(data_to_save):
    curent_time = datetime.now()
    if os.name == 'nt':
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        save_path = desktop + '\Credentials ' + curent_time.strftime("%Y-%d-%B") + '.txt'
        logs_txt = open(save_path, 'a')
        with logs_txt:
                logs_txt.write(data_to_save)
