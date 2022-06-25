import React from 'react';
import { Layout, Form, Input, Button } from 'antd';
import { SearchOutlined as SearchIcon} from '@ant-design/icons';

const Home = () => {
    const { Content, Footer } = Layout;
    
    return (
        <Layout>
            <div className='backgroundImg'>
                <div className='search-form'>
                    <Form layout='inline' labelCol={{ span: 12 }} >
                        <Form.Item name={'movieName'} label='Movie Name: '><Input placeholder="Movie Name" /></Form.Item>
                        <Form.Item name={'genre'} label='Genre: '><Input placeholder="Genre" /></Form.Item>
                        <Form.Item name={'actor'} label='Actor: '><Input placeholder="Actor" /></Form.Item>
                        <Form.Item name={'description'} label='Description: '><Input placeholder="Description" /> </Form.Item>
                        <Button type="primary" htmlType="submit">
                            <SearchIcon />
                        </Button>
                    </Form>
                </div>
            </div>
            <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
        </Layout>
    )
}

export default Home;