from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)

# Delete Post
@app.route('/posts/delete/<id>')
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

# Create Post
@app.route('/posts', methods=['GET', 'POST'])
def get_posts():
    posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('/posts.html', posts = posts)

@app.route('/posts/new_post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        db.session.add(BlogPost(title=title, author=author, content=content))
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('/new_post.html')

# Update/Edit Post
@app.route('/posts/edit/<post_id>', methods=['GET', 'POST'])
def edit(post_id):

    post = BlogPost.query.get(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('/edit.html', post = post)


@app.route('/')
def index():
    return render_template('/index.html')

if __name__ == "__main__":
    app.run(debug=True)