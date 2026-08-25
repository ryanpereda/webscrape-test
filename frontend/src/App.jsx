import { useEffect, useState } from "react";


function App() {
  const [quotes, setQuotes] = useState([]);
  const [page, setPage] = useState(1);
  const [hasNextPage, setHasNextPage] = useState(false);
  const [error, setError] = useState(null);


  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/quotes/?page=${page}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch quotes");
        }

        return response.json();
      })
      .then((data) => {
        setQuotes(data.quotes);
        setHasNextPage(data.has_next_page);
        setError(null);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, [page]);


  function goToPreviousPage() {
    if (page > 1) {
      setPage(page - 1);
    }
  }


  function goToNextPage() {
    if (hasNextPage) {
      setPage(page + 1);
    }
  }


  return (
    <main>
      <h1>Quote Scraper</h1>

      <div>
        <button
          onClick={goToPreviousPage}
          disabled={page === 1}
        >
          Previous
        </button>

        <span> Page {page} </span>

        <button
          onClick={goToNextPage}
          disabled={!hasNextPage}
        >
          Next
        </button>
      </div>

      {error && <p>Error: {error}</p>}

      {quotes.map((quote, index) => (
        <div key={index}>
          <p>"{quote.text}"</p>
          <p>- {quote.author}</p>
        </div>
      ))}
    </main>
  );
}


export default App;