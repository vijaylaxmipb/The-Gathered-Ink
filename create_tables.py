from taskmanager import create_app, db

app = create_app()

# Create an application context
with app.app_context():
    db.create_all()  # Create all tables defined in the models
    print("Tables created successfully")
