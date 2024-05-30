from selenium import webdriver


def before_all(context):
    prefs = {
        'download.directory_upgrade': True,
    }
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')
    options.add_argument('incognito')
    options.add_argument('start-maximized')
    options.add_argument(
        'disable-features=DownloadBubble,DownloadBubbleV2')
    if 'headless' in context.config.userdata:
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('no-sandbox')
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
    else:
        options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs', prefs)
    context.driver = webdriver.Chrome(options=options)


def after_all(context):
    context.driver.quit()
