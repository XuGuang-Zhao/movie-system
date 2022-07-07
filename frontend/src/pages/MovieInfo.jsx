import React from 'react';


const MovieInfo = () => {
    const movieID = localStorage.getItem('movieID');
    return (
        <>
            this is movie {movieID}  info page
        </>
    )
}

export default MovieInfo;