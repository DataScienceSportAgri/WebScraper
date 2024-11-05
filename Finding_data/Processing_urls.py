def start_downloading_process(config):
    runners_data = init_base()
    for url in config.urls:
        runners_data_page = finding_data_with_config(url)
        runners_data.add(runners_data_page)
    runners_datas = ''
    return runners_datas