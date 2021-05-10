import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Homepage from "../components/homepage/index";

export default function Redirect() {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/">
            <Homepage />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}
