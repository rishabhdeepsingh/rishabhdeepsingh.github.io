import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route } from "react-router-dom";
import "./index.css";
import App from "./App";
import User from "./components/user";

ReactDOM.render(
  <BrowserRouter>
    <Route path="/" component={App} />
    <Route path="/user" component={User} />
  </BrowserRouter>,
  document.getElementById("root")
);
