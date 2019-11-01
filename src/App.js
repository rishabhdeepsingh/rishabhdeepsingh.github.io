import "./App.css";

import React from "react";

import { SideBar } from "./components/SideBar";

function App() {
  return (
    <div className="App">
      <SideBar
        onSelect={selected => {
          window.location.href = selected;
          console.log(selected.toString());
        }}
      />
    </div>
  );
}

export default App;
