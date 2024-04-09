import React, { useState, useEffect  } from 'react';
import './App.css';
import axios from 'axios';
import NavBar from './components/NavBar/NavBar';
import Home from './components/Home/Home';
import About from './components/About/About';
import Contact from './components/Contact/Contact';

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
    default:
      ViewComponent = Home;
      break;
  }

  useEffect(() => {
    const fetchItems = async () => {
      const result = await axios('http://localhost:8000/api/items/');
      setItems(result.data);
    };
    fetchItems();
  }, []);

  return (
    
    <div className="App">
      <header className="App-header">

        <NavBar setView={setView} />
        <ViewComponent />
        {items.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
      </header>
    </div>
  );
}

export default App;