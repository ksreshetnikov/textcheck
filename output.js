// client/src/App.js
import React, { useEffect, useState } from 'react';

function App() {
  const [results, setResults] = useState({ good: 0, bad: 0 });

  useEffect(() => {
    fetch('http://localhost:5000/results')
      .then(res => res.json())
      .then(data => setResults(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Good vs Bad Results</h1>
      <p>Good: {results.good}</p>
      <p>Bad: {results.bad}</p>
    </div>
  );
}

export default App;
