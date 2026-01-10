def test_flipkart_login_page_title(driver):
    try:
        driver.get("https://www.flipkart.com/")
        title = driver.title
        print(title)
        assert "Online Shopping" in title
    except Exception:
        driver.save_screenshot("reports/flipkart_login_failure.png")
        raise
