##این قسمت فقط برای ما اون صفحه مدنظر رو باز میکنه 

from playwright.sync_api import sync_playwright

def opening_browser():

    with sync_playwright() as playwright :
        
        browser = playwright.chromium.launch(headless = False)


        Theـintendedـpage = input("enter the url :  ")
        
        page = browser.new_page()

        page.goto(Theـintendedـpage)

        input("for exit enter the Enter")

        browser.close()


if __name__  == "__main__":
     opening_browser()