import { useEffect, useState } from "react";


function App() {
  const [quotes, setQuotes] = useState([]);
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/quotes/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to load quotes");
        }

        return response.json();
      })
      .then((data) => {
        setQuotes(data.quotes);
        setCount(data.count);
        setError(null);
      })
      .catch((error) => {
        setError(error.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);


  return (
    <main>
      <h1>Quote Scraper</h1>

      {loading && <p>Loading quotes...</p>}

      {error && <p>Error: {error}</p>}

      {!loading && !error && (
        <>
          <p>Total quotes: {count}</p>

          {quotes.map((quote, index) => (
            <div key={index}>
              <p>"{quote.text}"</p>
              <p>- {quote.author}</p>
            </div>
          ))}
        </>
      )}
    </main>
  );
}


export default App;