from app import get_app


if __name__ == "__main__":
    get_app().run('0.0.0.0',
                  port=5008,
                  debug=True)
