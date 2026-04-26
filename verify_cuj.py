import asyncio
from playwright.async_api import async_playwright

async def verify_glassmorphism():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            record_video_dir="/home/jules/verification/videos/",
            record_video_size={"width": 1280, "height": 720}
        )
        page = await context.new_page()

        await page.goto('http://localhost:4321/en/services/')
        await asyncio.sleep(2)  # Wait for load and animations

        # 1. Take screenshot of light mode
        await page.screenshot(path='/home/jules/verification/screenshots/light_mode.png')

        # 2. Hover over the first card to trigger 3D tilt
        card = page.locator('.service-card').first
        await card.hover()
        await asyncio.sleep(1) # Let 3D effect settle
        await page.screenshot(path='/home/jules/verification/screenshots/light_mode_hover.png')

        # 3. Toggle dark mode
        theme_toggle = page.locator('.theme-switch-wrapper')
        if await theme_toggle.count() > 0:
             await theme_toggle.click()
             await asyncio.sleep(1)

             # Take screenshot of dark mode
             await page.screenshot(path='/home/jules/verification/screenshots/dark_mode.png')

             # Hover in dark mode
             await card.hover()
             await asyncio.sleep(1)
             await page.screenshot(path='/home/jules/verification/screenshots/dark_mode_hover.png')

        await context.close()
        await browser.close()

asyncio.run(verify_glassmorphism())
