from app import create_app, db

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()
        from app.seed import seed_data
        seed_data()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
