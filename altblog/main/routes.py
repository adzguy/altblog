from flask import render_template, request, redirect, Blueprint, url_for
from altblog import db
from altblog.models import BlogPost
from altblog.main.forms import PostForm

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Alt Blog')


@main.route('/posts', methods=['GET', 'POST'])
def get_posts():
    posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('posts.html', title='All Posts', posts=posts)


# Create Post
@main.route('/posts/new_post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        content = form.content.data
        db.session.add(BlogPost(title=title, author=author, content=content))
        db.session.commit()
        return redirect(url_for('main.get_posts'))
    else:
        return render_template('new_post.html', title='Create New Post', form=form)


# Update/Edit Post
@main.route('/posts/edit/<post_id>', methods=['GET', 'POST'])
def edit(post_id):

    post = BlogPost.query.get(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('main.get_posts'))
    else:
        return render_template('edit.html', title='Edit Post', post=post)


# Delete Post
@main.route('/posts/delete/<id>')
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.get_posts'))

# if __name__ == "__main__":
#     main.run(debug=True)
