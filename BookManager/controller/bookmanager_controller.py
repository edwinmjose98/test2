import io

from flask import Flask, render_template, request, current_app, redirect, url_for, Response
# from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from werkzeug.exceptions import Unauthorized, NotFound

from BookManager.service.bookmanager_service import BookService
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_principal import Principal, identity_changed, Identity, UserNeed, RoleNeed, Permission, identity_loaded
from BookManager.model.user import User
from BookManager.utilities.access_control import AccessControl

app = Flask(__name__)
app.secret_key = 'secret_key'


login=LoginManager(app)
login.init_app(app)
login.login_view='login'


# Principal(app)

# admin_permission = Permission(RoleNeed('Admin'))

@app.errorhandler(Exception)
def framework_error(ex):
    if isinstance(ex, Unauthorized):
        return render_template("unauthorized.html")
    # elif isinstance(ex, PermissionDenied):
    #     return redirect("/noaccess")
    elif isinstance(ex, NotFound):
        return "<h1>Ooops...can’t reach this page</h1>"
    else:
        return render_template("unauthorized.html")

# @identity_loaded.connect_via(app)
# def on_identity_loaded(sender, identity):
#     # Set the identity user object
#     identity.user = current_user
#
#     # Add the UserNeed to the identity
#     if hasattr(current_user, 'id'):
#         identity.provides.add(UserNeed(current_user.id))
#
#     # Assuming the User model has a list of roles, update the
#     # identity with the roles that the user provides
#     if hasattr(current_user, 'Role'):
#         for role in current_user.Role:
#             identity.provides.add(RoleNeed(current_user.Role))

@login.user_loader
def load_user(id):
    return User.get(int(id))

@app.route("/")
def home():
    return render_template("login.html")



@app.route("/login", methods=["POST" , "GET"])
def login():
    if(request.method=="POST"):
        username=request.form['email']
        password = request.form['password']
        exist=BookService.check_username(username)
        # print(exist)
        # if(exist==1):
        #     pass
        # else:
        #     return "<h1>Incorrect Credentials!!! Please go back and try again!!</h1>"
        passworddb=BookService.get_password(username=username)
        # print(username)
        # print(passworddb)
        if exist==1 and passworddb==password:
            user=BookService.get_user(username)
            # print(user)
            # print(type(user))
            # print(current_user)
            login_user(user)
            # identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
            # print(user.id)
            # print((type(user.id)))
            # print(list(current_user.dicts()))
            # print((type(current_user)))
            # print(current_user.id)
            # print(current_user.Role)
            if current_user.Role=='Admin':
                return redirect(url_for("admin_page"))
            else:
                return redirect(url_for("customer_page"))
        else:
            return "<h1>Incorrect Credentials!!! Please go back and try again!!</h1>"
    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("login.html")

@app.route("/admin_page")
@login_required
@AccessControl.admin
# @admin_permission.require()
def admin_page():
    books=BookService.display()
    return render_template("admin.html", books=books)



@app.route("/customer_page")
@login_required
def customer_page():
    authors=BookService.display_auths()
    categories=BookService.display_cats()
    books=BookService.display()
    return render_template("customer_page.html", a=authors, c=categories,b=len(books))

@app.route("/user_registration", methods=['POST', 'GET'])
def user_registration():
    if(request.method == 'GET'):
        return render_template("user_registration.html", flag=0, dup=0)
    else:
        result = BookService.insert_customer(request.form['username'], request.form['password'])
        if(result==-1):
            return render_template("user_registration.html", flag=0, dup=1)
        else:
            return render_template("user_registration_success.html", flag=0)



@app.route("/admin_registration", methods=['POST','GET'])
@login_required
@AccessControl.admin
# @admin_permission.require()
def admin_registration():
    if(request.method == 'GET'):
        return render_template("user_registration.html",flag=1,dup=0)
    else:
        result=BookService.insert_admin(request.form["username"],request.form["password"])
        if(result==-1):
            return render_template("user_registration.html",flag=1,dup=1)
        else:
            return render_template("user_registration_success.html", flag=1)

@app.route("/buy", methods=['POST', 'GET'])
@login_required
def buy():
    if request.method == 'POST' or request.method == 'GET':
        typo = list(request.form)
        # print(request.form)
        # print(typo)
        # print(typo[0])
        # # print(typo[1])
        # print("in controller")
        if typo[0] == 'category':
            books = BookService.display_bycat(request.form[typo[0]])
            # print(books)
        elif typo[0] == 'author':
            books = BookService.display_byauth(request.form[typo[0]])
        else:
            books = BookService.display_byname(request.form[typo[0]])
        if books == -1 or len(books) == 0:
            return render_template("unavailable.html")
        else:
            return render_template("buy.html", books=books)

# @app.route("/admin")
# def admin():
#     books = BookService.display()
#     return render_template("admin.html", books=books)
#
# @app.route("/user")
# def user():
#     return render_template("customer_page.html")

@app.route("/add", methods=['POST', 'GET'])
@login_required
@AccessControl.admin
# @admin_permission.require()
def add():
    if request.method == 'POST':
        BookService.insert(name=request.form["name"], cat=request.form["category"], aut=request.form["author"])
        return render_template("add.html")
    else:
        return render_template("add.html")

@app.route("/delete", methods=['POST'])
@login_required
def delete():
    BookService.buy(list(request.form))
    return render_template("success.html")

# if request.method == 'POST' or request.method == 'GET':
#     typo = list(request.form)
#
#     if typo[0] == 'category':
#         books = BookService.display_cat(request.form[typo[0]])
#
#     else:
#         books = BookService.display_aut(request.form[typo[0]])
#
#     if books == -1 or len(books) == 0:
#         return render_template("unavailable.html")
#     else:
#         return render_template("buy.html", books=books)


@app.route('/plot.png')
@login_required
def plot_png():
    fig = BookService.create_figure1()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)


