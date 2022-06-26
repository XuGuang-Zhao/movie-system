import React, {useCallback} from "react";
import styled from "styled-components";
import {Button, Form, Input} from "antd";
import {SearchOutlined as SearchIcon} from '@ant-design/icons';
import {Content} from "antd/es/layout/layout";

export function SearchBox(onFinish) {
    return (
            <SearchContainer>
                <SearchForm layout='inline' labelCol={{span: 12}} onFinish={onFinish}>
                    <SearchFormItem name="name" label='Movie Name: '>
                        <Input placeholder="Movie Name"/>
                    </SearchFormItem>

                    <SearchFormItem name="genre" label='Genre: '>
                        <Input placeholder="Genre"/>
                    </SearchFormItem>

                    <SearchFormItem name="actor" label='Actor: '>
                        <Input
                            placeholder="Actor"/>
                    </SearchFormItem>

                    <SearchFormItem name="description" label='Description: '>
                        <Input placeholder="Description"/>
                    </SearchFormItem>

                    <SearchFormItem name="director" label='Director: '>
                        <Input placeholder="Director"/>
                    </SearchFormItem>

                    <SearchButton type="primary" htmlType="submit">
                        <SearchIcon/>
                    </SearchButton>
                </SearchForm>
            </SearchContainer>
    )
}


const SearchContainer = styled(Content)`
  width: 80%;
  border: 2px solid rgba(255, 255, 255, 0.3);
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 55px;
  padding: 15px 0 0 75px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  margin: 10px auto 0;
  box-shadow: 0 10px 5px rgba(0, 0, 0, 0.5);
`

const SearchForm = styled(Form)`
  margin-bottom: 15px;
    
`
const SearchFormItem = styled(Form.Item)`
  margin: 15px;
`

const SearchButton = styled(Button)`
  width: 80px;
  margin: 10px auto;
`
