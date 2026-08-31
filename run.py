# from flask import Flask
# app = Flask(__name__)
# @app.get("/")
# def home():
#     return{
#         "message": "Manufacturing ERP API is running"
#     }
from backend_manufacturing_erp_flask import create_app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
    