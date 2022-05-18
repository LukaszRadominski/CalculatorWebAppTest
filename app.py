from flask import render_template, Flask, url_for, request #import potrzebnych modułów , url jest niezbędne by połaczyć to co dzieje sie na stronie HTML z tym co ma robic funkcja 

app = Flask(__name__) # ROZPOCZĘCIE aplikacji 

@app.route("/simple")  # route == link == url to sa linki lub ozwala użytkownikom na dostęp do naszej aplikacji internetowej # 
def simple():
    #person = "ŁukaszR"
    #return person # na stronie pojawi sie wartiśc zmiennej bo to ja zwraca funkcja 
    return render_template("simple.html") #render_template- wyświetl szblon

@app.route("/calculate", methods=["post"]) # methods=["post"] - mówimy PYTHONOWI że akurat tą funkcję "calculate" ma połaczyc z HTML # metoda post bo rezultat tej funkcji ma być wysłany na podany url : "/calculateeee"
def calculate():
    first_number = int(request.form["firstNubmer"]) # ŁACZENIE DANYCH Z  HTML  z PY request - żądanie pobrania z formularza (form) html "input" o nazwie name = firstNubmer 
    operation = request.form["operation"] # ale to co popchodzi z request to jest strint int[] zamienia string na number
    second_number = int(request.form["secondNumber"])
    if operation=="plus": # czyli jeżeli mamy operację o value (w html) ="plus"
        result=first_number+second_number
        # return str(result) # zamiast return na końcu zwraca wartośc zmiennej result zamienionej spowrotem na string  #jak wpiszemu "operation" zwróci nazwę operacji wg value= ... - tj parametru z html
    elif operation=="minus":
        result=first_number-second_number
        # return str(result) # Flask nie zwraca liczb więc result musimy ponownie zamienić z int na str
    elif operation=="multipy":
        result=first_number*second_number
        # return render_template("simple.html", result=result) # przy mnożeniu > result nr 2 z tej funkcji przekazywany jest do parametru result któy jest w simple.html 
    elif operation=="divide":
        result=first_number/second_number
        # return str(result) # zamiast każdorazowego result można spisać 1 result 
    else:
        return "There is an error"
    return render_template("simple.html", result=result)




if __name__ == '__main__': # ZAKOŃCZENIE aplikacji 
    app.run(debug=True) # debug zwraca wiadomości o błedach  - w publicznym użytkowaniu wybrać False żeby ludzie nie widzieli info o błędach 







