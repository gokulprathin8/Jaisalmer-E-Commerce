import './index.css';
import 'bootstrap/dist/css/bootstrap.css';

import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from "react-redux";
import {applyMiddleware, compose, createStore} from "redux";
import {persistStore} from "redux-persist";
import {PersistGate} from "redux-persist/integration/react";
import reduxThunk from "redux-thunk";

import App from './App';
import reducers from "./redux/reducers";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store =
    createStore(reducers, composeEnhancers(applyMiddleware(reduxThunk)));

const persistor = persistStore(store);

ReactDOM.render(<Provider store = {store}><PersistGate persistor = {persistor}>
                <App /></PersistGate>
  </Provider>,
                document.getElementById('root'));