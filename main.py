from flask import Flask, request, render_template
from wtforms import StringField, validators
from flask_wtf import FlaskForm

app = Flask(__name__, template_folder='templates') # template dizinini bildirdik

# csrf için secret key gerekli
app.config['SECRET_KEY'] = b'x\xda\xa8\xa3zM\x8c0Qi\x7f\xe2J\x1f\xbf\xa9\x12L;^(|\xb5f' 

# Formumuz tek bir fielddan oluşmakta ve validator formdaki fieldın boş gönderilmemesini istediğimiz için
class InputForm(FlaskForm):
    i_data = StringField("Data* ", validators=[validators.DataRequired()])


@app.route("/input-al", methods=["GET", "POST"])
def post_ile_input_al():
    if request.method == "POST":
        form = InputForm(request.form)
        if form.validate():
            my_data = form.i_data.data
            # burada my_data değişkeninde değerin var istediğin gibi kullan

            # Örnek olması için geri döndüreceğim sen istediğin şekilde kullanırsın sana kalmış
            return f"<h1> {my_data} </h1>"
            
        else:
            # formda hata çıkarsa eğer formu geri döndürcek içerisinde de hata mesajı var
            # template kısmında hata mesajı yazılacak bir yer var oraya mesajı yazacak
            # field : hata mesajı şekilde olur bu hata mesajları
            return render_template("input_icin_template.html", req=request, input_form=form)
    
    # Get isteği gelirse boş form döndürecek 
    return render_template("input_icin_template.html", req=request, input_form=InputForm())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080 ,debug=True) # 0.0.0.:8080 de çalışır

