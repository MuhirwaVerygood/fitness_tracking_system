const searchInput = document.getElementById('userSearchInput');
const userTableRows = document.querySelectorAll('#userTable tbody tr');

const rowsPerPage = 10; 
// Adjust this value to change the number of rows per page
let currentPage = 1;

searchInput.addEventListener('input', (e) => {
  const searchTerm = e.target.value.toLowerCase();
  userTableRows.forEach((row) => {
    const rowText = row.textContent.toLowerCase();
    if (rowText.includes(searchTerm)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
});
