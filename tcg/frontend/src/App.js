import React, { useState, useEffect  } from 'react';
import './App.css';
import axios from 'axios';
import NavBar from './components/NavBar/NavBar';
import Home from './components/Home/Home';
import About from './components/About/About';
import Contact from './components/Contact/Contact';
import Products from './components/Products/Products';

function App() {
  const [view, setView] = useState('home'); // 'home' is the default view
  const [items, setItems] = useState([]);

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
    case 'products':
      ViewComponent = Products;
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