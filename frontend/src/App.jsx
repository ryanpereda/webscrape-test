import { useEffect, useState } from "react";


function App() {
  const [quotes, setQuotes] = useState([]);
  const [error, setError] = useState(null);


  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/quotes/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch quotes");
        }

        return response.json();
      })
      .then((data) => {
        setQuotes(data.quotes);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, []);


  return (
    <main>
      <h1>Quote Scraper</h1>

      {error && <p>Error: {error}</p>}

      {quotes.map((quote, index) => (
        <div key={index}>
          <p>{quote.text}</p>
          <p>- {quote.author}</p>
        </div>
      ))}
    </main>
  );
}


export default App;