import random


def number_to_french(n):
    if n < 0 or n > 999999:
        return "Nombre hors de portée (0 - 999999 uniquement)."

    units = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
    teens = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
    tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]

    def below_hundred(n):
        if n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 70:
            if n % 10 == 1 and n != 71:
                return tens[n // 10] + "-et-" + units[n % 10]
            else:
                return tens[n // 10] + ("-" + units[n % 10] if n % 10 != 0 else "")
        elif n < 80:
            return "soixante-" + below_hundred(n - 60)
        else:
            # Handle numbers 80 to 99
            if n == 80:  # Special case for standalone 80
                return "quatre-vingts"
            elif n < 90:
                return "quatre-vingt" + ("-" + units[n - 80] if n % 10 != 0 else "")
            else:  # Numbers 90 to 99
                return "quatre-vingt-" + teens[n - 90]

    def below_thousand(n):
        if n == 0:
            return ""
        elif n < 100:
            return below_hundred(n)
        else:
            hundreds = n // 100
            remainder = n % 100
            if hundreds == 1:
                return "cent" + (" " + below_hundred(remainder) if remainder != 0 else "")
            else:
                return units[hundreds] + " cent" + (" " + below_hundred(remainder) if remainder != 0 else "")

    if n == 0:
        return "zéro"

    thousands = n // 1000
    remainder = n % 1000

    thousands_part = ""
    if thousands > 1:
        thousands_part = below_thousand(thousands) + " mille"
    elif thousands == 1:
        thousands_part = "mille"

    remainder_part = below_thousand(remainder)
    if thousands_part and remainder_part:
        return thousands_part + " " + remainder_part
    else:
        return thousands_part + remainder_part