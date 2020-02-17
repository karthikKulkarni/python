import json
from difflib import get_close_matches
import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

# cursor = con.cursor()
# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'rain'")
# results = cursor.fetchall()


def tarnslate(w):
    w = w.lower()
    cursor = con.cursor()
    query = cursor.execute(
        "SELECT * FROM Dictionary WHERE Expression = '%s'" % w)
    results = cursor.fetchall()

    data = results
    if len(data) > 0:
        val = ""
        for i in data:
            val = val + "\n" + i[1]

        return val
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(("Did you mean '%s' instead?" %
                    get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return tarnslate(get_close_matches(w, data.keys())[0])
        else:
            return "The word don't exist"
    else:
        return "The word don't exist"


print(tarnslate(input("Enter text:")))
