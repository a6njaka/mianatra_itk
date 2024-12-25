import os
import re
import glob
from fpdf import FPDF
import datetime


def create_dir(exo_dir):
    if not os.path.exists(exo_dir):
        os.makedirs(exo_dir)


def modify_answer(answer, casesencitive="Yes"):
    answer = re.sub(" +", " ", answer)
    if casesencitive == "True" or casesencitive == "Yes":
        answer = re.sub("([A-Z])", "\\1#", answer)
    return change_sp_char(answer)


def change_sp_char(text):
    answer = text
    answer = answer.replace(":", "%3A")
    answer = answer.replace("<", "%3C")
    answer = answer.replace(">", "%3E")
    answer = answer.replace("\"", "%22")
    answer = answer.replace("/", "%2F")
    answer = answer.replace("\\", "%5C")
    answer = answer.replace("|", "%7C")
    answer = answer.replace("?", "%3F")
    answer = answer.replace("*", "%2A")
    answer = answer.replace(">", "%3E")
    answer = answer.replace("?", "%3F")
    return answer


def change_sp_char2(text):
    answer = text
    answer = answer.replace("%3A", ":")
    answer = answer.replace("%3C", "<")
    answer = answer.replace("%3E", ">")
    answer = answer.replace("%22", "\"")
    answer = answer.replace("%2F", "/")
    answer = answer.replace("%5C", "\\")
    answer = answer.replace("%7C", "|")
    answer = answer.replace("%3F", "?")
    answer = answer.replace("%2A", "*")
    answer = answer.replace("%3E", ">")
    answer = answer.replace("%3F", "?")
    return answer


def config(exo_dir, maxstage=7, comment="Mianatra", rand="Yes", casesencitive="True", extra=""):
    if not os.path.exists(exo_dir):
        os.makedirs(exo_dir)
    try:
        f = open(exo_dir + '/stage_config.txt', 'w')
        f.write(f"MaxStage = {maxstage}\n")
        f.write(f"Comment = {comment}\n")
        f.write(f"CaseSensitive = {casesencitive}\n")
        f.write(f"Rand = {rand}\n")
        f.write(f"{extra}\n")
        f.close()
    except PermissionError:
        print("Error while creating config file")


def clean(exo_dir):
    files = []
    # r=root, d=directories, f = files
    # print("-" * 50)
    for r, d, f in os.walk(exo_dir):
        for file in f:
            m = re.match(r"^(B|A)[^A-Z].*\.[pngPNG]{3}", file)
            if m is not None:
                files.append(file)
                try:
                    os.remove(os.path.join(r, file))
                except FileNotFoundError:
                    print(f"The file \"{file}\" cannot be found")


def file_in_folder(folder, ext="png", start_with="", sort="az"):
    files_ret = list()
    os.chdir(folder)
    files = filter(os.path.isfile, os.listdir(folder))
    files = [os.path.join(f) for f in files]
    if sort == "time":
        files.sort(key=lambda x: os.path.getmtime(x))
    for text in files:
        m = re.match(f"({start_with}.*).{ext}$", text, re.I)
        if m is not None:
            files_ret.append(m.group(1))
    # for file in files:
    #     print(file)
    return files_ret


def exo_from_folder(folder, ext="png", sort="az"):
    files = list()
    files_ret = list()
    if sort == "az":
        for (dirpath, dirnames, filenames) in os.walk(folder):
            files += [file for file in filenames]
    elif sort == "time":
        files = list(filter(os.path.isfile, glob.glob(folder + "*.png")))
        files.sort(key=lambda x: os.path.getmtime(x))
    for f in files:
        filename, file_extension = os.path.splitext(f)
        if file_extension == ext:
            files_ret.append(filename)
    return files_ret


def upper_repl(match):
    return match.group(1).upper()


def generate_pdf(source_img, column=3, txt_start="B", sort_p="time", filename="exo_pdf"):
    print("--------------------------Images in PDF---------------------------")
    now = datetime.datetime.now()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.set_font('Helvetica', '', 8)
    # pdf.add_font('njk', '', 'D:/PROGRAMMING/PYTHON/Itokiana/Cursive standard.ttf', uni=True)
    # pdf.set_font('njk', '', 10)
    pdf.text(10, 5, f"ITOKIANA")
    pdf.text(180, 5, f"{now.day}/{now.month:02d}/{now.year}")
    pdf.set_font('Helvetica', '', 12)
    pdf.set_auto_page_break(False)
    col = 0
    i = 0
    for text in file_in_folder(source_img, start_with=txt_start, sort=sort_p):
        image = f"{source_img}{text}.png"
        print(image)
        if os.path.exists(image):
            # print(text)
            w = 190 / column
            h = w * 250 / 600
            cell_h = 9
            x0 = 10
            y0 = 10
            x = x0 + (w * (i % column))
            y = y0 + ((h + cell_h) * col)
            pdf.set_xy(x, y)
            if pdf.get_y() > (297 - h - cell_h - 10):
                x = x0
                y = y0
                col = 0
                i = 0
                pdf.add_page()
                pdf.set_xy(x, y)
            pdf.image(image, x, y, w)
            pdf.cell(w, h, "", 1, 2, "C")

            text = re.sub(r"(^B\d+-)", "", change_sp_char2(text))
            text = text.lower()

            text = re.sub(r"([a-z])#", upper_repl, text)

            pdf.cell(w, cell_h - 3, text, 1, 1, "C")
            if (i + 1) % column == 0:
                col += 1
            i += 1

    pdf.output(f'{source_img}{filename}.pdf', 'F')
    pdf.close()


def num_to_letter(i, genre="un"):
    if i == 0: return "zéro"
    if i == 1: return genre
    if i == 2: return "deux"
    if i == 3: return "trois"
    if i == 4: return "quatre"
    if i == 5: return "cinq"
    if i == 6: return "six"
    if i == 7: return "sept"
    if i == 8: return "huit"
    if i == 9: return "neuf"
    if i == 10: return "dix"
    if i == 11: return "onze"
    if i == 12: return "douze"
    if i == 13: return "treize"
    if i == 14: return "quatorze"
    if i == 15: return "quinze"
    if i == 16: return "seize"
    if i == 17: return "dix-sept"
    if i == 18: return "dix-huit"
    if i == 19: return "dix-neuf"
    if i == 20: return "vingt"
    if i == 21: return f"vingt-et-{genre}"
    return "---"
