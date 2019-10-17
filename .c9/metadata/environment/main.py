{"filter":false,"title":"main.py","tooltip":"/main.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":141,"column":0},"action":"insert","lines":["from flask import Flask, request, jsonify","from flask import Blueprint, render_template","from extensions import mongo","from bson.objectid import ObjectId","","from base64 import b64encode","import os","","file64 = None","","app = Flask(__name__)","","main = Blueprint('main', __name__)","","","@main.route('/')","def index():","    categories = mongo.db.categories.find({})","    bigTrends = list(mongo.db.recipes.find({}))","    for recipe in bigTrends:","        if recipe['image'] is None:","            recipe['image'] = \"\"","            ","    return render_template('index.html', bigTrends=bigTrends, categories=categories)","","","@main.route('/search')","def search():","    search = request.args.get('search')","    recipes = mongo.db.recipes.find({'name': {'$regex': \".*\"+search+\".*\"}})","","    return render_template('search.result.html', recipes=recipes)","","@main.route('/searchCategories/<categories>')","def searchCategories(categories):","    recipes = mongo.db.recipes.find({'categories': { '$in': categories.split(',')}})","","    return render_template('search.result.html', recipes=recipes)","    ","","@main.route('/searchCategoriesCount', methods=['POST'])","def searchCategoriesCount():","    categories = request.form.getlist('categories[]')","    ","    count = mongo.db.recipes.find({'categories': { '$in': categories}}).count()","    return  {'success': True, 'count': count}","    ","@main.route('/recipes')","def recipes():","    ","    recipes = list(mongo.db.recipes.find({}))","    for recipe in recipes:","        if recipe['image'] is None:","            recipe['image'] = \"\"","    ","    return render_template('recipe-list.html', recipes=recipes)","","@main.route('/recipe/<id>')","def recipe(id):","    recipe = mongo.db.recipes.find_one({'_id': ObjectId(id)})","    if recipe['image'] is None:","        recipe['image'] = \"\"","","    return render_template('recipe-details.html', recipe=recipe)","","","@main.route('/recipe/new')","def recipeNew():","","    return render_template('recipe-save.html')","","@main.route('/recipe/edit/<id>')","def recipeEdit(id):","    recipe = mongo.db.recipes.find_one({'_id': ObjectId(id)})","","    categories = [d.encode() for d in recipe['categories']]","    ","    return render_template('recipe-save.html', recipe=recipe)","    ","@main.route('/recipe/save', methods=['POST'])","def recipeSave():","","    recipe = {","        'name': request.form['name'],","        'time': request.form['time'],","        'ingredients': request.form['ingredients'],","        'preparation': request.form['preparation'],","        'categories': request.form.getlist('categories[]')","    }","    ","    if file64 != '':","        recipe['image'] = file64","    ","    id = request.form['id']","    ","    if id != \"\":","        mongo.db.recipes.update({'_id': ObjectId(id)},  {'$set': recipe}) ","    else:","        id = mongo.db.recipes.insert(recipe)","        ","    return {'success': True, 'id': str(id)}","","@main.route('/recipe/delete', methods=['POST'])","def recipeDelete():","    recipe = mongo.db.recipes.delete_one({'_id': ObjectId(request.form['id'])})","    ","    return {'success': True, 'id': str(id)}","    ","@main.route('/getRecipes')","def getRecipes():","    recipes = mongo.db.recipes.find({})","    ","    return recipes[0]['name']","","# Categories","@main.route('/categories/GetAll')","def categoriesGetAll():","    categories = mongo.db.categories.find({}).sort('name', 1)","    ","    output = []","    for category in categories:","        output.append(","            {'id': str(category['_id']), 'text': category['name']})","","    return jsonify(output)","","","@main.route('/file-upload', methods=['POST'])","def fileUpload():","    global file64","","    f = request.files.get('file')","    f.save(os.path.join('static/images', f.filename))","","    file64 = f.filename","    # if request.method == 'POST':","    #     image = request.files.get('file')","    #     file64 = b64encode(image.read())","    #f.save(os.path.join('the/path/to/save', f.filename))","","    return file64",""],"id":1}],[{"start":{"row":141,"column":0},"end":{"row":142,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":16,"column":12},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":23},"action":"insert","lines":["print(\"create_app\")"],"id":4}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":21},"action":"remove","lines":["create_app"],"id":5},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["i"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["n"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["d"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["e"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["x"]}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":[" "],"id":6},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["m"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["a"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["i"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["n"]}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"remove","lines":["."],"id":7}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["-"],"id":8}],[{"start":{"row":32,"column":34},"end":{"row":32,"column":35},"action":"remove","lines":["."],"id":9}],[{"start":{"row":32,"column":34},"end":{"row":32,"column":35},"action":"insert","lines":["-"],"id":10}]]},"ace":{"folds":[],"scrolltop":490.40625,"scrollleft":0,"selection":{"start":{"row":41,"column":30},"end":{"row":41,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":159,"mode":"ace/mode/python"}},"timestamp":1571348143203,"hash":"36f6e0a9af37bcc2c9adfb66a3b5eb6fb5948063"}