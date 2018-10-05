 
import os, inspect
import json
from flask import render_template, jsonify
from reb import app

import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd
from sklearn.externals import joblib
from keras.models import load_model
import tensorflow as tf
from keras import backend





# get project root dir
CURR_DIR = os.path.dirname(inspect.getabsfile(inspect.currentframe()))
ROOT_DIR = os.path.dirname(CURR_DIR)


# monthly date range generator
def month_range(start_date, n_months):
    for m in range(n_months):
        yield start_date + relativedelta(months=+m)

# home route
@app.route("/home")
@app.route("/index.html")
@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict/PAYEMS/<variables>/<target>")
def predict_payemns(variables, target):
    print(variables)
    print(target)

    d = {"a": [1, 2, 3], "b": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/W875RX1/<variables>/<target>")
def predict_w875rx1(variables, target):
    print(variables)
    print(target)

    d = {"d": [1, 2, 3], "e": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/INDPRO/<variables>/<target>")
def predict_indpro(variables, target):
    print(variables)
    print(target)

    d = {"f": [1, 2, 3], "g": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/CMRMTSPL/<variables>/<target>")
def predict_cmrmtspl(variables, target):
    print(variables)
    print(target)



    d = {"h": [1, 2, 3], "j": [4, 5, 6]}
    return jsonify(d)


@app.route("/predict/<variables>/<target>")
def predict(variables, target):

    variables = "8,2"
    target = "0"

    index_features = [int(elem) for elem in variables.split(',')]
    index_features.sort()
    index_target = int(target)


    # read data
    ffname = os.path.join(CURR_DIR, "data", "ext", "data_monthly_processed.csv")
    df = pd.read_csv(ffname, parse_dates=["DATE"])
    df.DATE = pd.to_datetime(df.DATE, format="%Y-%m")

    # Reindex data frame per the time stamps
    df.set_index("DATE", inplace=True)

    # load scaler
    ffname = os.path.join(CURR_DIR, "data", "int", "monthly.scaler.save")
    scaler = joblib.load(ffname)

    # rescale data
    all_values = df.values.astype("float32")
    all_values_scaled = scaler.fit_transform(all_values)

    # set model parameters
    n_lags = 6
    n_sequences = 6
    n_units = 10
    print(index_features)
    print(index_target)

    # get -lag samples
    x_scaled = all_values_scaled[-n_lags:, index_features + [index_target]]
    print("x_scaled shape: ", x_scaled.shape)
    n_variables = x_scaled.shape[1]
    # reshape x as per lstm input format
    x_scaled = x_scaled.reshape((1, n_lags, n_variables))
    print("x_scaled shape: ", x_scaled.shape)

    with backend.get_session().graph.as_default() as g:
        # load model
        fname = 'f.' + '.'.join([str(elem) for elem in index_features]) + \
                f'.t.{index_target}.l.{n_lags}.s.{n_sequences}.u.{n_units}' + '.h5'
        ffname = os.path.join(CURR_DIR, "data", "int", fname)
        print(fname)
        model = load_model(ffname)
        # forecast
        yhat_scaled = model.predict(x_scaled)

    print("modeld loaded")
    print("yhat_scaled shape: ", yhat_scaled.shape)

    # invert scaling
    temp = all_values_scaled[-n_sequences:, :]
    n_allvars = temp.shape[1]
    temp = temp.reshape((1, -1))
    temp[:, index_target:n_sequences * n_allvars:n_allvars] = yhat_scaled.reshape((1, n_sequences))
    temp = temp.reshape((-1, n_allvars))
    yhat = scaler.inverse_transform(temp)[:, index_target]

    # create forecast data frame
    df_forecast = pd.DataFrame()
    start_date = df.index[-1]
    mrange = month_range(start_date, n_sequences + 1)
    df_forecast["DATE"] = [d.strftime('%Y-%m-%d') for d in mrange]
    df_forecast["VALUE"] = list(df.values[-1:, index_target]) + list(yhat)
    df_forecast.set_index("DATE", inplace=True)
    df_forecast.head(n_sequences)

    # store data as dict
    data = {"current": [{"t": t, "x": x} for t, x in zip(list(df.index.astype(str).values),
                                                         df.iloc[:, index_target].astype("float32"))],
            "predict": [{"t": t, "x": x} for t, x in zip(list(df_forecast.index.astype(str).values),
                                                         df_forecast.VALUE.astype("float32"))]}


    # ffname = os.path.join(ROOT_DIR, "reb", "data", "int", "sample_data.json")
    # with open(ffname) as fp:
    #     data = json.load(fp)
    del model

    return jsonify(data)



