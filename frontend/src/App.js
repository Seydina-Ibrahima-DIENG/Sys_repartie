import React, { useEffect, useState } from 'react';

function App() {
  const [products, setProducts] = useState([]);

  // Cette fonction va appeler ton API Flask
  useEffect(() => {
    fetch('/api/products')
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error("Erreur API:", error));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Ma Plateforme Répartie</h1>
      <h2>Liste des Produits (depuis le Backend) :</h2>
      <ul>
        {products.length > 0 ? (
          products.map(p => (
            <li key={p.id}>{p.name} - {p.price}€</li>
          ))
        ) : (
          <li>Chargement des produits ou aucune donnée trouvée...</li>
        )}
      </ul>
    </div>
  );
}

export default App;
