import React from 'react';

function NavBar({ setView }) {
  return (
    <nav>
      <button onClick={() => setView('home')}>Home</button>
      <button onClick={() => setView('about')}>About</button>
      <button onClick={() => setView('contact')}>Contact</button>
    </nav>
  );
}

export default NavBar;