import React from 'react';
import MovieCard from "../component/MovieCard";
import styled from "styled-components";
import { SearchBox } from "../component/SearchBox";
import { FilterBox } from '../component/FilterBox';
import { OrderBox } from '../component/OrderBox';
import { Empty } from 'antd';

const SearchResult = () => {
  const movieList = JSON.parse(localStorage.getItem('movie_list')) || '';
  const filterList = JSON.parse(localStorage.getItem('filter_list')) || '';

  return (
    <Container>
      <SearchBox />
      {
        movieList.length === 0 ? (
          <EmptyPromote
            image="https://gw.alipayobjects.com/zos/antfincdn/ZHrcdLPrvN/empty.svg"
            imageStyle={{
              height: 60,
            }}
            description={
              <span>
                No Search result
              </span>
            }
          >
          </EmptyPromote>) :
          (<>
            <FilterBox filterList={filterList} />
            <OrderBox movieList={movieList} />
          </>)
      }
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
  flex-direction: column;
`;

const StyledMovieCard = styled.div`
  padding: 20px 0 0 80px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: flex-start;
`
const MovieItem = styled.div`
  margin: 20px;
`
const EmptyPromote = styled(Empty)`
  margin: 40px auto 0;
`