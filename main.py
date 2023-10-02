from playwright.sync_api import sync_playwright

while True:
    p = sync_playwright().start()
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://viz.flowics.com/public/7cdb790cceb696f76ec147008429eed8/650b2cf01b9b89db3a006742/live")
    vote_selector = page.locator(".answers .answer").all()[4]
    vote_selector.click()
    page.close()
    p.stop()




