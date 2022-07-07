import { Checkbox, Form, Row, Col, Button } from "antd";
import React, { useCallback } from "react";
import styled from "styled-components";
import { Content } from "antd/es/layout/layout";
import { SearchOutlined as SearchIcon } from '@ant-design/icons';
import { useLocation, useHistory } from 'react-router-dom';
import qs from 'query-string';
import { Request } from "../api/request";


export function FilterBox(filterList) {
    const filterArr = filterList.filterList;
    const actors = filterArr.filter(item => item.category === 'Actor').slice(0, 5);
    const directors = filterArr.filter(item => item.category === 'Director').slice(0, 5);
    const genres = filterArr.filter(item => item.category === 'Genre');
    const { search } = useLocation();
    const url = `/search/${search}`;
    const history = useHistory();
    const onFinish = useCallback((values) => {
        console.log("values", values);
        const actor_filter = values.actor ? values.actor.toString() : "";
        const director_filter = values.director ? values.director.toString() : "";
        const genre_filter = values.genre ? values.genre.toString() : "";
        localStorage.setItem('actor_filter', actor_filter);
        localStorage.setItem('director_filter', director_filter);
        localStorage.setItem('genre_filter', genre_filter);
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
            order_by: ''
        }

        Request('POST', ContentData, '/search/filter').then(data => {
            if (data) {
                localStorage.setItem('movie_list', JSON.stringify(data.movie_list));
                history.push(url);
            }
        })
    }, [history, search, url]);

    return (
        <FilterContainer>
            <FilterForm layout='inline' onFinish={onFinish} >
                <Form.Item name="actor" label='Actors: '>
                    <Checkbox.Group>
                        <Row>
                            {
                                actors.map(item => (
                                    <Col key={item.name}>
                                        <Checkbox value={item.name} style={{ lineHeight: '32px' }}>
                                            {item.name} ({item.count})
                                        </Checkbox>
                                    </Col>
                                ))
                            }
                        </Row>
                    </Checkbox.Group>
                </Form.Item>
                <Form.Item name="director" label='Directors: '>
                    <Checkbox.Group>
                        <Row>
                            {
                                directors.map(item => (
                                    <Col key={item.name}>
                                        <Checkbox value={item.name} style={{ lineHeight: '32px' }}>
                                            {item.name} ({item.count})
                                        </Checkbox>
                                    </Col>
                                ))
                            }
                        </Row>
                    </Checkbox.Group>
                </Form.Item>
                <Form.Item name="genre" label='Genres: '>
                    <Checkbox.Group>
                        <Row>
                            {
                                genres.map(item => (
                                    <Col key={item.name}>
                                        <Checkbox value={item.name} style={{ lineHeight: '32px' }}>
                                            {item.name} ({item.count})
                                        </Checkbox>
                                    </Col>
                                ))
                            }
                        </Row>
                    </Checkbox.Group>
                </Form.Item>
                <SearchButton type="primary" htmlType="submit">
                    <SearchIcon />
                </SearchButton>
            </FilterForm>
        </FilterContainer>
    )
}

const FilterContainer = styled(Content)`
  width: 60%;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  border: 2px solid #c4c7ce;
  background-color: #fff;
  border-radius: 15px;
  padding: 15px 0 0 75px;
  margin: 12px auto 0;
`
const FilterForm = styled(Form)`
  flex-direction: column;
`

const SearchButton = styled(Button)`
  display: table;
  width: 140px;
  margin: 10px auto;
`
