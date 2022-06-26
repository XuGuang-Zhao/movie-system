import React, { useCallback } from 'react';
import { Layout, Form, Input, Button } from 'antd';
import { SearchOutlined as SearchIcon } from '@ant-design/icons';
import { useHistory } from 'react-router-dom';
import styled from "styled-components";
import qs from 'query-string';

const Home = () => {
    const { Content, Footer } = Layout;
    const history = useHistory();
    const onFinish = useCallback((values) => {
        const { name, genre, actor, description, director } = values;
        const queryStr = qs.stringify(values);
        const url = `/search/?${queryStr}`;

        fetch('http://localhost:5000/search/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name || '',
                genre: genre || '',
                actor: actor || '',
                director: director || '',
                description: description || '',
            }),
        })
            .then(r => r.json())
            .then(data => {
                if (data.error) {
                    console.log(data.error);
                } else {
                    history.push(url);
                    localStorage.setItem('movie_list', JSON.stringify(data.movie_list));
                    localStorage.setItem('filter_list', JSON.stringify(data.filter_list));
                }
            })
    }, [history])

    return (
        <Layout>
            <div className='backgroundImg'>
                <Content>
                    <SearchContainer>
                        <SearchForm labelCol={{ span: 12 }} onFinish={onFinish}>
                            <SearchFormItem name="name" label='Movie Name: '><SearchInputBox placeholder="Movie Name" /></SearchFormItem>
                            <SearchFormItem name="genre" label='Genre: '><SearchInputBox
                                placeholder="Genre" /></SearchFormItem>
                            <SearchFormItem name="actor" label='Actor: '><SearchInputBox
                                placeholder="Actor" /></SearchFormItem>
                            <SearchFormItem name="description" label='Description: '><SearchInputBox
                                placeholder="Description" /></SearchFormItem>
                            <SearchFormItem name="director" label='Director: '><SearchInputBox placeholder="Director" /></SearchFormItem>
                            <SearchButton type="primary" htmlType="submit">
                                <SearchIcon />
                            </SearchButton>
                        </SearchForm>
                    </SearchContainer>
                </Content>
            </div>
            <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
        </Layout>
    )
}

export default Home;

const SearchContainer = styled.div`
  width: 80%;
  border: 2px solid rgba(255, 255, 255, 0.3);
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 55px;
  padding: 15px 0 0 75px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  margin: 50px auto 0;
  box-shadow: 0 10px 5px rgba(0, 0, 0, 0.5);
`

const SearchForm = styled(Form)`
  flex-direction: column;
`
const SearchFormItem = styled(Form.Item)`
  display: table;
  margin: 0 auto;
`

const SearchInputBox = styled(Input)`
  width: 200px;
`
const SearchButton = styled(Button)`
  display: table;
  width: 140px;
  margin: 10px auto;
`
