import React from 'react';
import './App.css';
import {SideBar} from "./components/SideBar";

function App() {
    return (
        <div className="App">
            <SideBar onSelect={(selected) => {
                console.log(selected.toString());
            }}/>
        </div>
    );
}

export default App;
