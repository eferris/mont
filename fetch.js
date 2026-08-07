fetch(API_URL)
  .then(response => response.json())
  .then(data => {
    // 1. Normalize payload into a consistent Array
    const items = Array.isArray(data) ? data : [data];

    // 2. Process using array methods safely
    items.forEach(item => {
      console.log('Processing item:', item);
    });
  })
  .catch(error => console.error('Error fetching data:', error));