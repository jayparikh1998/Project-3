# dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, render_template
from sqlalchemy import create_engine
from config import postgres_password, postgres_user, postgres_database, postgres_host

# Flask class instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_database}'
db = SQLAlchemy(app)

# models
class price(db.Model):
    __tablename__ = 'price'
    asin = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    currency = db.Column(db.Text)
    value = db.Column(db.Numeric)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in db.inspect(self).mapper.column_attrs}
    
class ratings(db.Model):
    __tablename__ = 'ratings'
    asin = db.Column(db.Text, primary_key=True)
    rating = db.Column(db.Numeric)
    ratings_total = db.Column(db.Integer)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in db.inspect(self).mapper.column_attrs}
    
class category(db.Model):
    __tablename__ = 'category'
    asin = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in db.inspect(self).mapper.column_attrs}
    
class bestsellers_books(db.Model):
    __tablename__ = 'bestsellers_books'
    asin = db.Column(db.Text)
    title = db.Column(db.Text, primary_key=True)
    author = db.Column(db.Text)
    cover = db.Column(db.Text)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in db.inspect(self).mapper.column_attrs}
    

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data_route():
    table1 = price.query.all()
    table2 = ratings.query.all()
    table3 = category.query.all()
    table4 = bestsellers_books.query.all()
    data = {'price': [row.to_dict() for row in table1],
            'ratings': [row.to_dict() for row in table2],
            'category': [row.to_dict() for row in table3],
            'bestsellers_books': [row.to_dict() for row in table4]}
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404