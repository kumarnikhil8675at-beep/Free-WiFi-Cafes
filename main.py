from flask import Flask,render_template,request,redirect,url_for,abort,jsonify
from flask_bootstrap import Bootstrap5
from database import db,cafe,User,rating
from functools import wraps
from flask_login import current_user,login_user,LoginManager,logout_user
from form import cafe_form,Sign,login
from werkzeug.security import check_password_hash,generate_password_hash
import os

app=Flask(__name__)
bootstrap=Bootstrap5(app)

login_manager=LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get("DB_URI","sqlite:///cafes.db")
app.config['SECRET_KEY'] = "rerraertrtre4aewertafdfsz"

db.init_app(app)

with app.app_context():
    db.create_all()
    
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,user_id)
#this is login manager decorater


def log_sig(fn):
    @wraps(fn)
    def start():
        if current_user.is_authenticated :
            return abort(404)
        return fn()
    return start

def page_access(fn):
    @wraps(fn)
    def start():
        if current_user.is_authenticated:
            return fn()
        return abort(404)
    return start
            

########################################

@app.route("/")
def home():
    coffe=db.session.execute(db.select(cafe)).scalars().all()
    print(current_user)
    return render_template("index.html",info=coffe,current=current_user)

@app.route("/update_cafe/<int:cafe_send>",methods=["GET","POST"])
def update(cafe_send):
    if current_user.is_authenticated:
        for so in current_user.cafe_id:
            print(so.id)
            if so.id == cafe_send:
                cc=db.get_or_404(cafe,cafe_send)
                form=cafe_form(obj=cc)
                
                if form.validate_on_submit():
                    form.populate_obj(cc)
                    db.session.commit()
                    user_loger_cafes = current_user.cafe_id
                    return render_template("User.html",info=user_loger_cafes,current=current_user)
        
                return render_template("cafeupdate.html",form=form,current=current_user)
    else: return abort(404)

@app.route("/login",methods=["GET","POST"])
@log_sig
def loger():
    form=login()
    if form.validate_on_submit():
        Name=form.name.data
        password=form.password.data
        
        user_loger=db.session.execute(db.select(User).where(Name == User.Name)).scalar()
        if user_loger:
            if check_password_hash(user_loger.Password,password):
                login_user(user_loger) 
                user_loger_cafes = current_user.cafe_id
                return render_template("User.html",info=user_loger_cafes,current=current_user)
    return render_template("login.html",form=form,current=current_user)

@app.route("/sing_in",methods=["GET","POST"])
@log_sig
def sing():
    form=Sign()

    if form.validate_on_submit():
        user_Data=User(
            Name=form.name.data,
            Password=generate_password_hash(form.password.data, method='scrypt',salt_length=8) 
        )
        db.session.add(user_Data)
        db.session.commit()
        login_user(user_Data)
        user_loger_cafes = current_user.cafe_id
        return render_template("User.html",info=user_loger_cafes,current=current_user)
    return render_template("sing.html",form=form,current=current_user)

@app.route("/add_cafe",methods=["GET","POST"])
@page_access
def addd():
    form=cafe_form()
    if form.validate_on_submit():
        add_cafe=cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
            m_user=current_user
        )
        db.session.add(add_cafe)
        db.session.commit()
        user_loger_cafes = current_user.cafe_id
        return render_template("User.html",info=user_loger_cafes,current=current_user)
    
    return render_template("cafe_add.html",form=form,current=current_user)


@app.route("/rating/<int:cafe_id>", methods=["POST"])
def rasting(cafe_id):
    if not current_user.is_authenticated:
        return jsonify({"success": False, "error": "Login required"}), 401

    quantity = int(request.form["quantity"])

    com = db.session.execute(
        db.select(rating).where(
            (rating.who_rate == current_user.id) &
            (rating.who_cafe == cafe_id)
        )
    ).scalar()

    if com:
        com.ratting = quantity
    else:
        h = rating(
            ratting=quantity,
            user=current_user,
            who_cafe=cafe_id
        )
        db.session.add(h)

    db.session.commit()

    # Is cafe ki saari ratings dobara calculate karo
    all_ratings = db.session.execute(
        db.select(rating).where(rating.who_cafe == cafe_id)
    ).scalars().all()

    total = sum(r.ratting for r in all_ratings)
    count = len(all_ratings)
    average = total / count if count else 0

    return jsonify({
        "success": True,
        "average": average,
        "count": count
    })


@app.route("/dashboard")
@page_access
def dashboard():
    user_loger_cafes = current_user.cafe_id
    return render_template("User.html",info=user_loger_cafes,current=current_user)

@app.route("/logout")
@page_access
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/about")
def about():
    return render_template("about.html",current=current_user)

if __name__ == "__main__":
    app.run(debug=True)