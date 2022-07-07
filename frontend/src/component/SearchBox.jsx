import React, { useEffect } from "react";
import styled from "styled-components";
import { Button, Form, Input } from "antd";
import { SearchOutlined as SearchIcon } from '@ant-design/icons';
import { Content } from "antd/es/layout/layout";
import { useLocation, useHistory } from 'react-router-dom';
import { useCallback } from "react";
import qs from 'query-string';
import { Request } from "../api/request";

export function SearchBox() {
    const history = useHistory();
    const [form] = Form.useForm();
    const { search } = useLocation();
    const searchParam = qs.parse(search);
    
    useEffect(()=>{
        form.setFieldsValue(searchParam);
    }, [form, searchParam]);

    const onFinish = useCallback((values) => {
        const { name, genre, actor, description, director } = values;
        const queryStr = qs.stringify(values);
        const url = `/search/?${queryStr}`;
        const ContentData = {
            name: name || '',
            genre: genre || '',
            actor: actor || '',
            director: director || '',
            description: description || '',
        }
        Request('POST', ContentData, '/search/search').then(data => {
            if (data) {
                history.push(url);
                localStorage.setItem('actor_filter', "");
                localStorage.setItem('director_filter', "");
                localStorage.setItem('genre_filter', "");
                localStorage.setItem('movie_list', JSON.stringify(data.movie_list));
                localStorage.setItem('filter_list', JSON.stringify(data.filter_list));
            }
        })
    }, [history])

    return (
        <SearchContainer>
            <SearchForm form={form} layout='inline' labelCol={{ span: 12 }} onFinish={onFinish}>
                <SearchFormItem name="name" label='Movie Name: '>
                    <Input placeholder="Movie Name" />
                </SearchFormItem>
                <SearchFormItem name="genre" label='Genre: '>
                    <Input placeholder="Genre" />
                </SearchFormItem>
                <SearchFormItem name="actor" label='Actor: '>
                    <Input placeholder="Actor" />
                </SearchFormItem>
                <SearchFormItem name="description" label='Description: '>
                    <Input placeholder="Description" />
                </SearchFormItem>
                <SearchFormItem name="director" label='Director: '>
                    <Input placeholder="Director" />
                </SearchFormItem>
                <SearchButton type="primary" htmlType="submit">
                    <SearchIcon />
                </SearchButton>
            </SearchForm>
        </SearchContainer>
    )
}


const SearchContainer = styled(Content)`
  width: 60%;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  border: 2px solid #c4c7ce;
  background-color: #fff;
  border-radius: 15px;
  padding: 15px 0 0 75px;
  margin: 12px auto 0;
`

const SearchForm = styled(Form)`
  margin-bottom: 12px;
`
const SearchFormItem = styled(Form.Item)`
  margin: 12px;
`

const SearchButton = styled(Button)`
  width: 80px;
  margin: 12px auto;
`
