import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(null);
  const [file, setFile] = useState(null);

  const handleFileChange = async (e) => {
    console.log('this is the file');
    const file = e.target.files[0];
    if (file) {
        setFile(file);

        const formData = new FormData();
        formData.append('file', file);

        try {
          fetch('http://localhost:5000/api/time').then(res => res.json()).then(data => {
            setCurrentTime(data.time);
          });
            // Process the extractedText and set benefits
        } catch (error) {
            console.error("Error uploading and parsing the file:", error);
        }
    }
};

  return (
    <div className="App">
      <header className="App-header">
        <BrowserRouter>
          <div>
            <Link className="App-link" to="/">Home</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/page2">Page2</Link>
          </div>
          <Switch>
            <Route exact path="/">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                  Edit <code>src/App.js</code> and save to reload.
                </p>
                <input
                    type="file"
                    accept=".pdf"
                    onChange={handleFileChange}
                    className="uploadButton"
                />
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
                <p>The current time is {currentTime}.</p>
            </Route>
            <Route path="/page2">
                <p>This is page 2!</p>
            </Route>
          </Switch>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
