import React from 'react';

const SearchResult = () => {
    const movieList = JSON.parse(localStorage.getItem('movie_list')) || '';
    const filterList = JSON.parse(localStorage.getItem('filter_list')) || '';
    return (
        <div>
            This is Search Result Page!
        </div>
    )
}

export default SearchResult;