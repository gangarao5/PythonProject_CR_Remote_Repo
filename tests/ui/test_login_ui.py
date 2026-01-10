def test_flipkart_login_page_title(driver):
    driver.get("https://www.flipkart.com/")
    title = driver.title
    print(title)
    assert "Online Shopping" in title
