def click_on_alert(driver, button_text):
    driver.execute_script(f"""
        document.querySelectorAll('button').forEach(function(button) {{
            if (button.textContent.includes("{button_text}")) {{
                button.click();
            }}
        }});
    """)


def send_keys_in_confirm(driver, keys):
    driver.execute_script(f"""
        window.prompt = function(message, defaultValue) {{
            return '{keys}';
        }};
    """)
