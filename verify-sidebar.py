from playwright.sync_api import sync_playwright
import time
import os

def test_sidebar():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:4321')
        time.sleep(2)

        # Test 1: Hover behavior
        print("Testing hover behavior...")
        sidebar = page.locator('#sidebar-nav')
        sidebar_box = sidebar.bounding_box()
        page.mouse.move(sidebar_box['x'] + sidebar_box['width'] / 2, sidebar_box['y'] + sidebar_box['height'] / 2)
        time.sleep(1)

        # Take a screenshot to see hover state
        page.screenshot(path='hover_state.png')
        print(f"Sidebar classes after hover: {sidebar.get_attribute('class')}")

        # Test 2: Lock behavior
        print("Testing lock behavior...")
        lock_btn = page.locator('#sidebarLockBtn')
        lock_btn.click()
        time.sleep(1)

        # Take a screenshot to see locked state
        page.screenshot(path='locked_state.png')
        print(f"Sidebar classes after lock: {sidebar.get_attribute('class')}")
        print(f"Body classes after lock: {page.locator('body').get_attribute('class')}")

        # Get computed width of main-content
        main_content_width = page.evaluate('window.getComputedStyle(document.querySelector(".main-content")).width')
        print(f"Main content width after lock: {main_content_width}")

        browser.close()

if __name__ == "__main__":
    test_sidebar()
