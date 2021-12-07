class RegularPageLocators:
    """
    regular page locators
    """
    template = "//span[text()= 'About Us 01']//ancestor::div[@role = 'button']"
    page_in_page_list = "//span[text()='{}']//ancestor::div[@class='Polaris-ResourceItem__Container']//button[not(@aria-label)]"
