import os


class Config:
    # basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'  # + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
