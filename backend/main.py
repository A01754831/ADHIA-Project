import sqlite3
from datetime import date
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
from typing import Literal
import joblib
import numpy as np

class RestaurantSearchModel(BaseModel):
    terms: str
    
class Restaurant(BaseModel):
    id: int
    name: str

class RestaurantTransactionsModel(BaseModel):
    restaurant_id: int
    start_date: date
    end_date: date

class PredictionModel(BaseModel):
    stars: int
    total: float
    wifi: Literal["Yes", "No"]
    alcohol: Literal["Yes", "No"]
    valet: Literal["Yes", "No"]

def create_connection():
    conn = sqlite3.connect("data.db")
    return conn

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def load_classification_model():
    return joblib.load("rf_model.joblib")

def load_restaurants_from_csv():
    try:
        # Asegúrate de que el archivo CSV esté en la misma carpeta o proporciona la ruta completa
        #df = pd.read_csv('TOTAL.csv',usecols=['id', 'name'])
        #return df.to_dict(orient='records')
        df = pd.read_csv('TOTAL.csv')
        df = df.loc[:, ['id', 'name']]
        return df.values.tolist()
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []
    

app = FastAPI()



# Endpoint para obtener la lista de restaurantes desde el CSV
@app.get("/api/restaurantes")
async def get_restaurants():
    restaurants = load_restaurants_from_csv()
    return {"restaurants": restaurants}  # Devuelve la lista de restaurants

@app.post("/restaurant_search")
def restaurant_search(search: RestaurantSearchModel):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    terms = search.terms.split()
    terms = " OR ".join(terms)
    query = "SELECT rowid, Name FROM restaurants_fts WHERE restaurants_fts MATCH ? ORDER BY rank"
    cursor.execute(query, (f"{terms}",))
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/restaurant/{restaurant_id}")
def restaurant(restaurant_id: int):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT  r.* FROM restaurant r WHERE r.id = ?"
    cursor.execute(query, (restaurant_id, ))
    results = cursor.fetchone()
    conn.close()
    return results

@app.get("/restaurant/{restaurant_id}/image", response_class=FileResponse)
def restaurant_image(restaurant_id: int):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT Image FROM restaurants WHERE ID = ?"
    cursor.execute(query, (restaurant_id, ))
    results = cursor.fetchone()
    conn.close()
    return FileResponse(f"images/{results["Image"]}")

@app.post("/predict")
def predict(prediction: PredictionModel):
    try:
        rf_model = load_classification_model()

        # Codificación de las variables categóricas
        wifi_coded = 1 if prediction.wifi == "Yes" else 0
        alcohol_coded = 1 if prediction.alcohol == "Yes" else 0
        valet_coded = 1 if prediction.valet == "Yes" else 0

        pred_df = pd.DataFrame([{
            "stars": prediction.stars,
            "total_bill": prediction.total,
            "wifi_coded": wifi_coded,
            "alcohol_coded": alcohol_coded,
            "valet_coded": valet_coded,
        }])
        
        rf_model_pred = rf_model.predict(pred_df)[0]
        rf_model_pred = int(rf_model_pred) if isinstance(rf_model_pred, np.generic) else rf_model_pred

        return {"classification": rf_model_pred}

    except Exception as e:
        return {"error": f"Error al procesar la solicitud: {str(e)}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)