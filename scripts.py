click_on_alert = """
    document.querySelectorAll('button').forEach(function(button) {{
        if (button.textContent.includes("{keys}")) {{
            button.click();
        }}
    }});
"""

send_keys_in_prompt = """
    window.prompt = function(message, defaultValue) {{
        return '{keys}';
    }};
    """

get_element_by_id = """
    return document.getElementById('file-upload').value;
    """
