class ShopifyPageLocators:
    """
    login page locators
    """
    email = "input[type='email']"
    password = "input[type='password']"
    submit = "button[type='submit']"

    """
    admin locators
    """
    online_store_btn = "//span[text()='Online Store']"
    navigation_menu = "//span[text()='Navigation']"
    main_menu_btn = "//a[text()='Main menu']"
    add_menu_item_btn = "//span[text()='Add menu item']//parent::button"
    menu_name_input = "//input[@placeholder='e.g. About us']"
    choose_page_input = "//input[@placeholder='Search or paste a link']"
    pages_option = "//div[text()='Pages']"
    choose_page_from_option_btn = "//div[text()='{}']//ancestor::button"
    dismiss_message = "//button[@aria-label='Dismiss this message']"
    add_btn = "//span[text()='Add']/ancestor::button"
    save_menu_btn = "//span[text()='Save menu']//ancestor::button"
    view_online_store_btn = "//a[@aria-label='View your online store']"
    online_store_iframe = "//iframe[@title = 'Online Store']"
    customer_menu = "//span[text()='Customers']"
    find_customer = "//input[@placeholder='Filter customers']"
    customer_search_result = "//div[text()='{}']"

    """
    store locators
    """
    menu_with_text = "//span[text()='{menu_name}']"
    page_buider_page = "div.apb_body"
    powered_by_automizely = "//span[text()= 'Powered by Automizely']"
    email_input = ".apb_customer_form_input"
    subscribe_btn = ".apb_customer_form_submit_button"
    page_in_menu = "//a[contains(text(),'{}')]"
    preview_bar_iframe = "#preview-bar-iframe"
    close_preview_bar = "//button[contains(text(),'Hide bar')]"
    coupon_code = "//input[@value='{}']"
    products_added_to_list_section = ".apb_product_list_product_item"
