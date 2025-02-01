CLICK_ON_ALERT = """
    document.querySelectorAll('button').forEach(function(button) {{
        if (button.textContent.includes("{keys}")) {{
            button.click();
        }}
    }});
"""

SEND_KEYS_IN_PROMPT = """
    window.prompt = function(message, defaultValue) {{
        return '{keys}';
    }};
    """

GET_ELEMENT_BY_ID = """
    return document.getElementById('file-upload').value;
    """
