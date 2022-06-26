import React from 'react';
import {MovieListCard} from "../component/MovieCard";
import styled from "styled-components";

const SearchResult = () => {
    const movieList = JSON.parse(localStorage.getItem('movie_list')) || '';
    const filterList = JSON.parse(localStorage.getItem('filter_list')) || '';

    console.log(movieList);
    // console.log(filterList);

    return (
        <Container>
            This is Search Result Page!
            <StyledMovieCard>
                {
                    movieList.map(movie => (
                        <MovieItem key={movie.id}>
                            <MovieListCard movieData={movie}/>
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
