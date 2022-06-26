import React, {useCallback, useState} from 'react';
import MovieCard from "../component/MovieCard";
import styled from "styled-components";
import {SearchBox} from "../component/SearchBox";

const SearchResult = () => {
    const movieList = JSON.parse(localStorage.getItem('movie_list')) || '';
    // const filterList = JSON.parse(localStorage.getItem('filter_list')) || '';

    return (
        <Container>
            <SearchBox/>
            <StyledMovieCard>
                {
                    movieList.map(movie => (
                        <MovieItem key={movie.id}>
                            <MovieCard movieData={movie}/>
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
  flex-direction: column;
`;

const StyledMovieCard = styled.div`
  padding-top: 20px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
`
const MovieItem = styled.div`
  margin: 20px;
`
