config.load_autoconfig(False)
config.set("colors.webpage.darkmode.enabled", True)
c.url.searchengines = {'DEFAULT': 'https://searx.org/?q={}'}
c.url.default_page = "https://searx.org/"
c.url.start_pages = "https://searx.org/"
config.set('content.javascript.enabled', False)
