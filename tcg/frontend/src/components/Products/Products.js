import axios from 'axios';
import React, { useState, useEffect  } from 'react';



function Products() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchItems = async () => {
      const response = await axios('http://localhost:8000/api/products/');
      setItems(response.data);
    };
    fetchItems();
  }, []);

  return (
    <div>
      <h1>Products</h1>
      <p>All products will be displayed here!</p>
      <ul>
          {items.map(items => 
            (<li key={items.id}>
            {items.name} - ${items.price}
            </li>))}

        </ul>
    </div>
  );
}

export default Products;