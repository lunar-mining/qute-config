config.load_autoconfig(False)
config.set("colors.webpage.darkmode.enabled", True)
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}
c.url.default_page = "duckduckgo.com"
c.url.start_pages = "duckduckgo.com"
config.set('content.javascript.enabled', False)
