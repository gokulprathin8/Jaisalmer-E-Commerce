import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";

// const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

// const store = createStore(
//   reducers,
//   composeEnhancers(applyMiddleware(reduxThunk))
// );

// const persistor = persistStore(store);

ReactDOM.render(
  <div>
    <App />
  </div>,
  document.getElementById("root")
);
