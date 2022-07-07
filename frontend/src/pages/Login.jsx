import React, { useState, useCallback, useContext} from 'react';
import { Button, Input, message } from 'antd';
import { useHistory } from 'react-router-dom';
import { Request } from '../api/request';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import { UserContext } from '../utils/reducer';


const Login = () => {
  const { dispatch } = useContext(UserContext);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();
  const onFinish = useCallback(() => {
    const ContentData = {
      username: username,
      password: password,
    }
    Request('POST', ContentData, '/user/login').then(data => {
      if (data) {
        localStorage.setItem('userID', data.user_id);
        dispatch({ type: 'userID', userID: data.user_id });
        message.success("Welcome back " + data.username);  
        history.push('/');
      }
    })
  }, [dispatch, history, password, username])


  return (
    <div className="login">
      <p className='login-title'>Login</p>
      <div className='login-wrapper'>
        <Input id='username' prefix={<UserOutlined className="site-form-item-icon" />} value={username} onChange={(value) => setUsername(value.target.value)} placeholder='Email' className='login-input' />
        <Input id='password' prefix={<LockOutlined className="site-form-item-icon" />} value={password} onChange={(value) => setPassword(value.target.value)} type='password' placeholder='Password' className='login-input' />
        <Button onClick={onFinish} className='login-button'>Submit</Button>
      </div>
    </div>
  );
};

export default Login;



