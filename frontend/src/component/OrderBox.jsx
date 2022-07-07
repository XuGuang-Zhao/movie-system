import React, {useCallback} from "react";
import { Content } from "antd/es/layout/layout";
import styled from "styled-components";
import { Select } from 'antd';
import { useLocation, useHistory } from 'react-router-dom';
import qs from 'query-string';
import { Request } from "../api/request";


export function OrderBox(param) {
    const movieArr = param.movieList;
    const movieCount = movieArr.length;
    const { Option } = Select;
    const { search } = useLocation();
    const url = `/search/${search}`;
    const history = useHistory();
    
    const onChange = useCallback((values) => {
        const genre_filter = localStorage.getItem("genre_filter") || '';
        const actor_filter = localStorage.getItem("actor_filter") || '';
        const director_filter = localStorage.getItem("director_filter") || '';
        const order_by = values || '';
        const { name, genre, actor, description, director } = qs.parse(search.slice(1));
        const ContentData = {
            search_request: {
                name: name || '',
                genre: genre || '',
                actor: actor || '',
                director: director || '',
                description: description || '',
            },
            genre_filter: genre_filter || '',
            actor_filter: actor_filter || '',
            director_filter: director_filter || '',
            order_by: order_by,
        }
        
        Request('POST', ContentData, '/search/filter').then(data => {
            if (data) {
                localStorage.setItem('movie_list', JSON.stringify(data.movie_list));
                history.push(url);
            }
        })
    }, [history, search, url]);
    
    return (
        <OrderContainer>
            <SearchTips>Results:  {movieCount} movies was found</SearchTips>
            <OrderByBox>
                <Select
                    placeholder="Order by"
                    size="large"
                    style={{width: '180px'}}
                    onChange = {onChange}
                >
                    <Option value="alpha_asc">Movie Name : A-Z</Option>
                    <Option value="alpha_desc">Movie Name : Z-A</Option>
                    <Option value="avg_rating_desc">Rating desc</Option>
                </Select>
            </OrderByBox>
        </OrderContainer>
    )

}

const OrderContainer = styled(Content)`
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: 18px;
  width: 85%;
  display: flex;
  justify-content: space-between;
  margin: 20px auto 0;
`

const SearchTips = styled.div`
`

const OrderByBox = styled.div`
`