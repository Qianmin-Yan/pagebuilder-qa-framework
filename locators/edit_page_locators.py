class EditPageLocators:
    form_coupon_input = "//input[contains(@name,'couponCode')]"
    form_with_coupon_option = "//input[@value='customCoupon']//parent::span"
    form_without_coupon_option = "input[value='noCoupon']"
    added_product_in_product_detail = "//div[contains(@class, 'ProductDetailContainer_product_list')]"
    div_contain_text = "//div[text()='{}']"
    delete_button = ".Polaris-Card__Subsection .Polaris-Button"
    page_name = "#title"
    publish_btn = "//span[text()='Published']//preceding-sibling::span/span"
    save_btn = "//span[text()='Save']"
    first_save_popup_modal = ".Polaris-Modal-Section"
    go_to_shopify_admin_btn = "//span[text()='Go to Shopify admin']"
    done_it_btn = "//span[contains(text(), 'done it')]"
    images_inside_shadow_root = "div[class*='container']+div::shadow img"
    preview = "div[class^='container']+div"
    preview_wrapper = 'div[class^="Previewer_previewer_wrapper"]'
    live_chat = ".crisp-client"
    publish_successfully_modal = "span[aria-label='congratulate']"
    span_contain_text = "//span[text()='{}']"
    confirm_to_publish_home_page_modal = "//p[text()='You already have a published homepage. If you confirm, your existing homepage will be unpublished.']"
    checkbox_in_product_chosen_modal = "(//div[@class='Polaris-ResourceItem__Container']//span[@class='Polaris-RadioButton__Backdrop'])[{}]"
    added_product_in_product_list = ".Polaris-Card__Subsection"
    section_add_button = "div[style='opacity:1'] button"
    content_tab = "#Content"
    settings_tab = "#Settings"
    style_tab = "#Style"
    back_button = "button[aria-label='back']"
    page_status = '.Polaris-VisuallyHidden-Badge'
    added_product_title = "//div[contains(@class, 'SelectedProductList_product_title')]"