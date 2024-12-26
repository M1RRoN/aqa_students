from pages.dynamic_content import DynamicContent


def test_dynamic_content(driver):
    dc = DynamicContent(driver)
    driver.get(dc.URL)
    src_list = driver.all_elements(dc.URL, "img", "src")
    print(src_list[1:3])
    for i in range(1, 10):
        if src_list[0] == src_list[1] and src_list[0] == src_list[2]:
            assert src_list[0] == src_list[1]
            break
        elif src_list[1] == src_list[0] and src_list[1] == src_list[2]:
            assert src_list[1] == src_list[2]
            break
        elif src_list[2] == src_list[0] and src_list[2] == src_list[1]:
            assert src_list[2] == src_list[0]
            break
        else:
            driver.refresh()
            src_list = driver.all_elements(dc.URL, "img", "src")
