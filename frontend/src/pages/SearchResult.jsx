import React from 'react';
import MovieCard from "../component/MovieCard";
import styled from "styled-components";

const SearchResult = () => {
    const movieList = JSON.parse(localStorage.getItem('movie_list')) || '';
    // const filterList = JSON.parse(localStorage.getItem('filter_list')) || '';
    
    return (
        <Container>
            <StyledMovieCard>
                {
                    movieList.map(movie => (
                        <MovieItem key={movie.id}>
                            <MovieCard movieData={movie} />
                        </MovieItem>
                    ))
                }
            </StyledMovieCard>
        </Container>
    )
}

export default SearchResult;

const Container = styled.div`
  display: flex;
  margin: 10px;
`;

const StyledMovieCard = styled.div`
  padding-top: 20px;
  display: flex;
  flex-wrap: wrap;
`
const MovieItem = styled.div`
  margin: 20px;
`
