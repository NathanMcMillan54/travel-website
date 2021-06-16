def format_text(text):
    formatted_text = str(text.to_dict(flat=False))
    final_text = formatted_text.replace("{'Form': ['", "").replace("']}", "")
    return final_text


def log_input(form_input):
    text = format_text(form_input)
