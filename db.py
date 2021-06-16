import main
import os


def format_text(text):
    formatted_text = str(text.to_dict(flat=False))
    final_text = formatted_text.replace("{'Form': ['", "").replace("']}", "")
    return final_text


def log_input(form_input):
    text = format_text(form_input)
    byte_file = open("db/byte_db.txt", "a")
    byte_file.writelines(f"{text}\n")
    print(f"Name: {eval(text)[0]} Email: {eval(text)[1]} Budget: {eval(text)[2]}")
    os.system(f'echo sqlite3 db/empty_main_db.sql "insert into travler values ({main.id_number}, "test", "test", 1.2);"')
