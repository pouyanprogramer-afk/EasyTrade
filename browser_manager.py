##این قسمت فقط برای ما اون صفحه مدنظر رو باز میکنه 
from pathlib import Path
from playwright.sync_api import sync_playwright

def opening_browser():
    
    profile_path =Path(__file__).resolve().parent / ".browser_profile"

    with sync_playwright() as playwright :
        my_URL = input("enter the URL : ")
        
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=str(profile_path),
            headless = False,
                  )
       
        page = context.pages[0] if context.pages else context.new_page()

        page.goto(my_URL)

        input("for exit enter the Enter")

        context.close()


if __name__  == "__main__":
     opening_browser()