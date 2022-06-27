import {message} from 'antd';

export function Request(method, data, specificUrl,) {
    const action = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(
            data
        ),
    };

    return fetch(`http://localhost:5000${specificUrl}`, action)
        .then(response => response.json())
        .then((data) => {
            if (data.error) {
                message.error(data.error);
                return;
            }
            return data;
        }).catch(e => message.error(e.message));
}

