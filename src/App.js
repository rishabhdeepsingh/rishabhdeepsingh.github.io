import React from "react";
import "./App.css";
import { SideBar } from "./components/sideBar";

function App() {
  return (
    <div className="App">
      <SideBar
        onSelect={(selected) => {
          window.location.href = selected;
          console.log(selected.toString());
        }}
      />
    </div>
  );
}

export default App;
