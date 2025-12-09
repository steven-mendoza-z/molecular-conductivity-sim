"""
Entry point for the application.
"""
import src.ui.app as app

def main():
    app_instance = app.MainApp([])

    app_instance.run_app()
    

if __name__ == "__main__":
    main()
