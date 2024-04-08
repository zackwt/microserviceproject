import React, { useState } from 'react';
import './App.css';
import NavBar from './components/NavBar/NavBar';
import Home from './components/Home/Home';
import About from './components/About/About';
import Contact from './components/Contact/Contact';

function App() {
  const [view, setView] = useState('home'); // 'home' is the default view

  let ViewComponent;

  // Determine which component to show based on the current view
  switch (view) {
    case 'home':
      ViewComponent = Home;
      break;
    case 'about':
      ViewComponent = About;
      break;
    case 'contact':
      ViewComponent = Contact;
      break;
    default:
      ViewComponent = Home;
      break;
  }

  return (
    
    <div className="App">
      <header className="App-header">
        <NavBar setView={setView} />
        <ViewComponent />
      </header>
    </div>
  );
}

export default App;